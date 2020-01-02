import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DLAP-0064;'
                      'Database=QUAN_LY_NHAN_VIEN;'
                      'Trusted_Connection=yes;')


class Container:
    containerNumber = ""
    containerHeight = ""
    containerType = ""
    containerWeight = ""
listContainer = []

def inputContainer():
    while(True):

        #Tap doi tuong c cho phep luu tru thong tin container
        c =  Container()
        c.containerNumber = input("Nhap so container: ")
        c.containerType = input("Nhap loai container: ")
        c.containerWeight = input("Nhap khoi luong container: ")
        c.containerHeight = input("Nhap chieu cao container: ")
        listContainer.append(c)

        #User can input thong tin de xac nhan nhap tiep hay ko
        print("Ban co muon nhap tiep container? 'OK' de tiep tuc: ")
        i = input()
        if i == "OK":
            continue
        else:
            break

def printListOfContainer(listCon):
    for i in listCon:
        print(i.containerNumber, " - ", i.containerHeight, " - ", i.containerType, " - ", i.containerWeight)
    print("Xong roai!!!")

def writeInformation(listCon):
    f = open("DanhSach.txt", mode='w+')
    stringToWrite = ""
    for i in listCon:
        stringToWrite = stringToWrite + i.containerNumber + " - "+ i.containerHeight + " - " + i.containerType+ " - " + i.containerWeight + "\n"
    f.write(stringToWrite)
    f.close()
    print("Xong roai!!!")

def insertDatabase(listCon):
    cursor = conn.cursor()
    for i in listCon:
        s = "INSERT INTO CONTAINER(containerNumber, containerHeight, containerType, containerWeight) VALUES("+ "'"+ i.containerNumber+"'" + ","+ "'"+i.containerHeight+"'"+ ","+ "'"+ i.containerType+"'"+ ","+ "'" + i.containerWeight+ "'"+ ")"
        cursor.execute(s)
        conn.commit()
    print("Xong roai!!!")

def selectContainerFromDatabase():
    cursor = conn.cursor()
    s = "SELECT * FROM CONTAINER"
    cursor.execute(s)
    result = cursor.fetchall()
    for r in result:
        print(r)


while(True):
    print("Vui long chon chuc nang: ")
    print("0. Thoat chuong trinh")
    print("1. Nhap container")
    print("2. In danh sach container")
    print("3. Ghi danh sach container xuong file txt")
    print("4. Ghi danh sach container xuong co so du lieu")
    print("5. Truy van danh sach container tu co du lieu")


    m = int(input())
    if m == 0:
        exit(1)
    elif m == 1:
        inputContainer()
    elif m == 2:
        if len(listContainer) == 0:
            print("Danh sach container rong")
        else:
            printListOfContainer(listContainer)
    elif m==3:
        if len(listContainer) == 0:
            print("Danh sach container rong")
        else:
            writeInformation(listContainer)
    elif m==4:
        if len(listContainer) == 0:
            print("Danh sach container rong")
        else:
            insertDatabase(listContainer)

    elif m==5:
        selectContainerFromDatabase()

