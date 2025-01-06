#Trang 4
print("#Trang 4")
print("VD1")
#xây dựng hàm trong python
def hello_MDC(str):
    print('Hi', str,', How are you?')
    print('Have a nice day!')
#sử dụng hàm đã xây dựng
hello_MDC('Tùng Dương')
#Trang 6
print("#Trang 6")
print("VD2")
#Xây dựng hàm tính n!
def giai_thua(n):
    tich = 1
    for i in range(1,n+1):
        tich = tich * i
    return tich

n = int(input('Nhập vào một số nguyên n: '))
print(n, '!=', giai_thua(n))

#Trang 7
print("#Trang 7")
print("VD3")
#Gọi hàm giai_thua đã xây dựng
print ('12! = ', giai_thua(12))

#Trang 9
print("#Trang 9")
print("VD4")
#Hàm tính tổng, hiệu, tích, thương:
def all_ab(a,b):
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    #hàm trả về kết quả là 4 giá trị
    return add, sub, mul, div

a = 10
b = 6
#lấy kết quả trả về khi thực hiện hàm
tong, hieu, tich, thuong = all_ab(a,b)
print('Tổng ',a, '+',b, '= ',tong)
print('Hieu ',a, '-',b, '= ',hieu)
print('Tích ',a, '*',b, '= ',tich)
print('Thuong ',a, '/',b, '= ',thuong)

#Trang 12
print("#Trang 12")
print("VD5")
#hàm tính tổng
def sum_ab(a = 5, b =7):
    total = a + b
    return total
#gọi hàm sum_ab
print(sum_ab(8,13))
print(sum_ab())

#Trang 13
print("#Trang 13")
print("VD6")

def get_sum(*num):
    tmp=0
    for i in num:
        tmp = tmp +1
    return tmp

ketqua = get_sum(1,2,3,4,5)
print('Kết quả ', ketqua)

#Trang 14
print("#Trang 14")
print("VD7")
x = 300
y = 800
def myfunc():
    x = 200
    total = x + y
    print('(Local) x :', x)
    print('total :', total)
myfunc()

print('------------------')
print('(global) x: ', x)

####
def myfunc():
    global k
    k = 300
    print('Inside k: ', k)
myfunc()
print('Outside func: k=', k)

#Trang 15
print("#Trang 15")
print("VD8")
x = lambda a:a+10
print(x(5))
print(x(7))

##
x = lambda a,b:a*b
print(x(5,6))