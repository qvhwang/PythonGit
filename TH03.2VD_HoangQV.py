#Trang 21

class Rectangle:
    def __init__(self, wigth, height):
        self.width = wigth
        self.height = height

    def getArea(self):
        area = round(self.width * self.height, 1)
        return area
    def getPerimeter(self):
        perimeter = round(2 * (self.width + self.height), 1)
        return perimeter

#Trang 26
r1 = Rectangle(10,5)
r2 = Rectangle(20,11)
x = r1.width
y = r1.height
print('-----Thuộc tính-------')
print('1. Thuộc tính Chiều rộng: ',x)
print('2. Thuộc tính Chiều cao: ', y)
dt = r1.getArea()
cv = r1.getPerimeter()
print('-----Phương thức-------')
print('1. Phương thức tinh diện tích: ', dt)
print('2. Phương thức tinh chu vi: ', cv)

#Trang 37
#1)
f = open('sieu quan trong.txt')
st = f.read()

print('Nội dung file: ')
print(st)

#2)
f = open('sieu quan trong.txt', "r")
st1 = f.read(10)
print(st1, ' --- Số ký tự là: ', len(st1))

#Trang 38
#1)
f = open('sieu quan trong.txt')
print(f.readline())
print(f.readline())
f.close()
#2)
f = open('sieu quan trong.txt', 'r')
for x in f:
    print(x)
f.close()

#Trang 39
f1 = open('sieu quan trong.txt', 'w')
st = 'Welcome to Python for Analyssis!'
f1.write(st)
f1.close()

#Trang 40
f1 = open('sieu quan trong.txt', 'a+')
st = 'This is new line....'
f1.write(st)
f1.close()
f = open("sieu quan trong.txt", "r")
print(f.read())

#Trang 41

f2 = open('sieu quan trong.txt')
print('1. Tên file:', f2.name)
print('2. Chế độ mở file:', f2.mode)
print('3. Trạng thái đóng file:', f2.closed)

#Trang 42

#1)
fo = open('data.txt', 'w')
fo.write('Tobe or not tobe. \n Nghi lon de thanh cong! \n')
fo.close()
print('Ghi file thành công!')

#2)
obj = open('sieu quan trong.txt', 'w')
obj.write("Chao mung cac ban den voi khoa CNTT")
obj.close()
obj1 = open('sieu quan trong.txt', 'r')
s = obj1.read()
print(s)
obj1.close()
obj2 = open('sieu quan trong.txt', 'r')
s1 = obj2.read(20)
print(s1)
obj2.close()