#Giai phuong trinh bac 1 ax+b = 0;

a = float(input('Vui long nhap a: '))
b = float(input('Vui long nhap b: '))

if a == 0 and b == 0:
    print('Phuong trinh vo so nghiem')
elif a == 0 and b != 0:
    print('Phuong trinh vo nghiem')
else:
    print('Phuong trinh cos 1 nghiem la: ', (-b/a))
