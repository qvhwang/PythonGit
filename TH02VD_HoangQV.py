#Trang 4
print("#Trang 4")
a = 10
b = 8
tong = a+b
hieu = a-b
tich = a*b
thuong = a/b 
thuong_nguyen = a//b
thuong_du = a%b
mu = a**b
print('Tong: ',tong)
print('Hieu: ',hieu)
print('Tich: ',tich)
print('Thuong: ',thuong)   
print('Thuong nguyen: ',thuong_nguyen)
print('Thuong du: ',thuong_du)
print('Mu: ',mu)

#Trang 6
print("#Trang 6")
a = 10
b = 8
print('1) Lớn hơn (a>b): ',a>b)
print('2) Nhỏ hơn (a<b): ',a<b)
print('3) Bằng (a==b): ',a==b)
print('4) Lớn hơn hoặc bằng (a>=b): ',a>=b)
print('5) Nhỏ hơn hoặc bằng (a<=b): ',a<=b)
print('6) Không bằng (a!=b): ',a!=b)

#Trang 7
print("#Trang 7")
x = 15
y = True

kt = (x>3) and (x<10)
kt2 = (x>3) or (x<10)
kt3 = not y
print('1) Phép toán AND: ',kt)
print('2) Phép toán OR: ',kt2)
print('3) Phép toán NOT: ',kt3)

#Trang 9
print("#Trang 9")
so_tien = input ('Nhập vào số tiền bạn có:  ')
so_tien = int(so_tien)
if (so_tien >= 1000000000):
    print('Bạn đã là một tỷ phú!')
else:
    print('Bạn còn phải kiếm nhiều tiền hơn!')

#Trang 10
print("#Trang 10")
print("#Dạng 1:")
print("#Điều kiện đúng!")
num = 3
if num > 0:
    print(num, "là số dương.")
print("Thông điệp này luôn được in.")

print("#Điều kiện sai!")
num = -1
if num > 0:
    print(num, "là số dương.")
print("Thông điệp này luôn được in.")

#Trang 11
print("#Trang 11")

so = int(input("Nhập số: "))
if(so % 2 == 0):
    print(so, "là số chẵn.")
else:
    print(so, "là số lẻ.")

#Trang 12
print("#Trang 12")
print("#Dạng 2:")
print("#Số dương")
num = 3
if num > 0:
    print("Số dương")
else:
    print("Số âm")

print("#Số âm")
num -1
if num > 0:
    print("Số dương")
else:
    print("Số âm")

#Trang 14
print("#Trang 14")
print("#Dạng 3:")

num = int(input("Nhập số nguyên: "))

if num > 0:
    print(num, "là số dương.")
elif num < 0:
    print(num, "là số âm.")

elif num == 0:
    print(num, "là số 0.")
else:
    print("Không phải số.") 

#Trang 15
print("#Trang 15")
num = int(input("Nhập số nguyên: "))
if num == 0:
    print("Chào anh đẹp trai!")
elif num == 1:
    print("Chào chị xinh gái!")
else:
    print("Cảnh báo: Giới tính không xác định!")

#Trang 16
print("#Trang 16")
num = float(input("Nhập một số: "))
if num >= 0:
    if num == 0:
        print("Số Không")
    else:
        print("Số dương")
else:
    print("Số âm")

#Trang 23
print("#Trang 23")
print("#Vòng lặp while")
n = int(input("Em sinh tháng mấy? "))
i = 1
while(i<=n):
    print(i, ') I Love You!')
    i=i+1

#Trang 24
print("#Trang 24")
print("#Lệnh break")

n = int(input("Em sinh tháng mấy? "))
i = 1
while(i<=n):
    print(i, ') I Love You!')
    if (i==3):
        break;
    i=i+1

#Trang 25
print("#Trang 25")
print("#Lệnh continue")

n = 20
i = 1
while(i<=n):
    i = i + 1
    if (i%3!=0):
        continue
    print(i)

#Trang 26
print("#Trang 26")
print("#Lệnh while true")
while True:
    n = int(input("Em sinh tháng mấy? "))
    if(1<=n<=12):
        break
    print("Tháng sinh không đúng, vui lòng nhập lại")
print("Chào em cô gái tháng", n)

#Trang 27
print("#Trang 27")
print("#Vòng lặp for")
n = 10
tich = 1
tong = 0
for i in range(1,n+1):
    tich = tich * i
    tong = tong + i
print("10!: ",tich)
print("10+: ",tong)

#Trang 28
print("#Trang 28")
print("#Vòng lặp for với chuỗi ký tự")
print("#VD1")
st = 'HUMG IN MY MIND'
for i in st:
    print('ký tự: ', i)

print("#VD2")
st = 'HUMG IN MY MIND'
dem = 0
for i in st:
    if (i == 'M'):
        dem = dem + 1
        print("Số ký tự M có trong chuỗi là: ", dem )

#Trang 29
print("#Trang 29")
print("#Vòng lặp for với danh sách")
hoc_sinh = ['Lê Thùy Dung', 'Trần Đức Hùng', 'Nguyễn Lan Anh', 'Mai Phương Thúy', 'Trần Thanh Thủy', 'Kiều Thành Công']
print('Danh sách học sinh bao gồm:')
tt = 1
for i in hoc_sinh:
    print(tt, ') ', i)
    tt = tt + 1

#Trang 31
print("#Trang 31")
print("#Vòng lặp for với lệnh range()")
print("#VD1")
for i in range(5):
    print('i = ', i)
print("#VD2")
for i in range(5,10):
    print('i = ', i)
print("#VD3")
for i in range(2,11,2):
    print('i = ', i)

#Trang 32
print("#Trang 32")
print("#Vòng lặp for lồng nhau")
for i in range(2,10):
    print('Bảng cửu chương ', i)
    for j in range(1,11):
        print(i, 'x', j, '=', i*j)
