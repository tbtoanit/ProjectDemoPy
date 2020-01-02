#Viet phuong trinh in ra so nguyen to lon nhat trong list cac so nguyen
listSN = [1,6,3,9,13,29,33,23,44,78,79,101]
listSNT = []

def kiemTraSNT(n):
    count = 0
    for i in range(2,n):
        if n%i == 0:
            count = count + 1;
            break
        if count > 0:
            return False
        else:
            return True

for i in listSN:
    if kiemTraSNT(i) == True:
        listSNT.append(i)

maxSNT = max(listSNT)

print("So nguyen to lon nhat la: ",maxSNT)
