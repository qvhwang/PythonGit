#Trang 35
import numpy as np
n = 12
matrix = np.random.randint(0, 101, size=(n, n), dtype=np.int32)
print("Ma trận:")
print(matrix)
print("\nKiểu dữ liệu của phần tử trong ma trận:", matrix.dtype)
print("Kích thước của mảng ma trận:", matrix.shape)
print("Số phần tử của mảng ma trận:", matrix.size)
print("Số chiều của mảng ma trận:", matrix.ndim)

#Trang 36
v_chinh = np.diagonal(matrix)
v_phu = np.fliplr(matrix).diagonal()
print("\nVector các phần tử nằm trên đường chéo chính:")
print(v_chinh)
print("\nVector các phần tử nằm trên đường chéo phụ:")
print(v_phu)

#Trang 37
while True:
    try:
        x = int(input("Nhập vào giá trị x (0-100): "))
        if 0 <=x<= 100:
            print("Giá trị x:", x)
            count_equal = np.sum(matrix == x)
            count_less = np.sum(matrix < x)
            count_greater = np.sum(matrix > x)
            print("------------------------------------")
            print(f"1. Số phần tử có giá trị bằng {x} trong ma trận: {count_equal}")
            print(f"2. Số phần tử nhỏ hơn giá trị {x} trong ma trận: {count_less}")
            print(f"3. Số phần tử lớn hơn giá trị {x} trong ma trận: {count_greater}")
            break
        else:
            print("Giá trị x phải trong khoảng 0-100")
            break
        
    except ValueError:
        print("Giá trị x phải là số nguyên")
        break