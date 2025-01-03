#slide 71
      #so,chuoi
a = 10
b = a
b = 5
print('Giá trị của biến a:', a)
print('Giá trị của biến b:', b)
      #danhsach 
ds_a = [4, 5, 8, 9]
ds_b = ds_a
ds_b[1] = 10
print('Biến ds_a:', ds_a)
print('Biến ds_b:', ds_b)
#slide 72
ds_a = [4, 5, 8, 9]
ds_b = ds_a.copy()
ds_b[1] = 10
print('Biến ds_a:', ds_a)
print('Biến ds_b:', ds_b)
#slide 73
x = True
y = False
z = 5 > 8
w = 12 == 12

print('Kiểu dữ liệu của biến x:', type(x), ', Giá trị: ', x)
print('Kiểu dữ liệu của biến y:', type(y), ', Giá trị: ', y)
print('Kiểu dữ liệu của biến z:', type(z), ', Giá trị: ', z)
print('Kiểu dữ liệu của biến w:', type(w), ', Giá trị: ', w)