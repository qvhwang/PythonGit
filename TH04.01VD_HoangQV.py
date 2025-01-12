#Trang 13

import numpy as np
a = np.array([1, 2, 5, 7, 0, 8])
print (a)
print ("Loại dữ liệu của biến a:", type(a))
print("Kiểu dữ liệu của phần tử trong mảng a: ", a.dtype)
print("Kích thước của mảng a:", a.shape)
print("Số phần tử của mảng a:", a.size)
print("Số chiều của mảng a:", a.ndim)

#Trang 14
import numpy as np
b = np.array([(4, 5, 6.0), (1, 2, 3.5)])
print (b)
print ("Loại dữ liệu của biến a:", type(b))
print("Kiểu dữ liệu của phần tử trong mảng a: ", b.dtype)
print("Kích thước của mảng a:", b.shape)
print("Số phần tử của mảng a:", b.size)
print("Số chiều của mảng a:", b.ndim)
   
#Trang 15
import numpy as np
c = np.array([[(2, 4, 0, 6), (4, 7, 5, 6)],
             [(0, 3, 2, 1), (9, 4, 5, 6)],
             [(5, 8, 6, 4), (1, 4, 6, 8)]])
print (c)
print ("Loại dữ liệu của biến a:", c[0, 0, 0])
print("Kiểu dữ liệu của phần tử trong mảng a: ", c.dtype)
print("Kích thước của mảng a:", c.shape)
print("Số phần tử của mảng a:", c.size)
print("Số chiều của mảng a:", b.ndim)

#Trang 18
#VD1
#1)
import numpy as np
array_zeros = np.zeros((2, 3))
print (array_zeros)
print("Kiểu dữ liệu của phần tử trong mảng a: ", array_zeros.dtype)
print("Kích thước của mảng a:", array_zeros.shape)
print("Số phần tử của mảng a:", array_zeros.size)
print("Số chiều của mảng a:", array_zeros.ndim)

#2)
import numpy as np
array_one = np.ones((2, 3), dtype = np.int32)
print (array_one)
print("Kiểu dữ liệu của phần tử trong mảng a: ", array_one.dtype)
print("Kích thước của mảng a:", array_one.shape)
print("Số phần tử của mảng a:", array_one.size)
print("Số chiều của mảng a:", array_one.ndim)

#Trang 19
#VD2
import numpy as np
array_eye = np.eye(5)
print (array_eye)
print("Kiểu dữ liệu của phần tử trong mảng a: ", array_eye.dtype)
print("Kích thước của mảng a:", array_eye.shape)
print("Số phần tử của mảng a:", array_eye.size)
print("Số chiều của mảng a:", array_eye.ndim)

#Trang 20
#VD3
import numpy as np
array_random = np.random.random((7,5))
print (array_random)
print("Kiểu dữ liệu của phần tử trong mảng a: ", array_random.dtype)
print("Kích thước của mảng a:", array_random.shape)
print("Số phần tử của mảng a:", array_random.size)
print("Số chiều của mảng a:", array_random.ndim)

#Trang 21
#VD4
import numpy as np
array_random = np.random.randint(low = 10, high= 30, size= 6, dtype= np.int32)
print (array_random)
print("Kiểu dữ liệu của phần tử trong mảng a: ", array_random.dtype)
print("Kích thước của mảng a:", array_random.shape)
print("Số phần tử của mảng a:", array_random.size)
print("Số chiều của mảng a:", array_random.ndim)

#Trang 22
#VD5
import numpy as np
d = np.arange(1, 25, 2)
print('Vector d = ', d)
print('Số phần tử của vector d:', d.size)

print('----------------------------')
f = np.linspace(1, 15, 11)
print('Vector f:', f)   
print('Số phần tử của vector f:', f.size)

#Trang 25
import numpy as np
path = 'data.txt'
diem_2a = np.loadtxt(path, delimiter = ',', dtype=np.int32)

print(diem_2a)
print("Kiểu dữ liệu của phần tử trong mảng a: ", diem_2a.dtype)
print("Kích thước của mảng a:", diem_2a.shape)
print("Số phần tử của mảng a:", diem_2a.size)
print("Số chiều của mảng a:", diem_2a.ndim)

#Trang 28
#1)
import numpy as np
a_float = np.linspace(0, 15, 11)
print('a_float')
print('Kiểu dữ liệu:', a_float.dtype)
print('---------------------------')
a_int = a_float.astype(np.int16)
print(a_int)
print('Dữ liệu sau khi chuyển:' , a_int.dtype)

#2)
import numpy as np
a_str = a_int.astype(str)
print(a_str)
print('Dữ liệu sau khi chuyển:', a_str.dtype)
print('---------------------------')
a_bol = a_int.astype(np.bool)
print(a_bol)
print('Dữ liệu sau khi chuyển:' , a_bol.dtype)

#Trang 31
#1)
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('Vector a = ', a)
print('Số phần tử của vector a: \n', a)
print('----------------------------')
print('phần tử đầu tiên:', a[0])
print('phần tử thứ 3:', a[3])
print('phần tử cuối cùng:', a[-1])

#2)
print('Số phần tử của vector a: \n', a)
print('----------------------------')
print('3 phần tử đầu tiên:', a[:3])
print('từ phần tử thứ 5 tới hết:', a[5:])
print('từ phần tử 2 đến phần tử <6 của vector:', a[2:6])

#Trang 32
import numpy as np
path = 'data.txt'
diem_2a = np.loadtxt(path, delimiter = ',', dtype=np.int32)

print(diem_2a)
print('Điểm môm học đầu tiên, của học sinh đầu tiên:', diem_2a[0, 0])
print('Điểm môn học thứ 1, của học sinh thứ 3:', diem_2a[1, 3])
print('Điểm môn học cuối, của học sinh cuối:', diem_2a[-1, -1])
print('----------------------------')
print('Bảng điểm lớp 2A: \n', diem_2a)

#Trang 33
diem_hs5 = diem_2a[:, 5]
print('Điểm các môn của học sinh 5: \n', diem_hs5)
diem_mon = diem_2a[-1, :]
print('Điểm môn học cuối cùng của tất cả học sinh: \n', diem_mon)
diem5_hs10 = diem_2a[:5,:10]
print('Bảng điểm 5 môn học đầu tiên của 10 học sinh đầu của lớp: \n', diem5_hs10)