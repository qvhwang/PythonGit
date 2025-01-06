#Trang 18
print("#Trang 18")
print("#Bài 6")

letters = str(input("Nhập một ký tự chữ: "))

#Trang 19
print("#Trang 19")
print("#Bài 7")

height = float(input("Nhập chieu cao: "))
weight = float(input("Nhập cân nặng: "))

BMI = weight / (height * height)

print("Chỉ số BMI của bạn là: ", BMI)
if BMI < 18.5:
    print("Underweight")
elif BMI > 18.5 and BMI < 24.9:
    print("Normal Weight")
elif BMI > 25 and BMI < 29.9:
    print("Overweight")
else:
    print("Obese")

#Trang 20
print("#Trang 20")
print("#Bài 8")

month = int(input("Nhập tháng sinh: "))
if month >= 1 and month <= 3:
    print("Bạn sinh vào Mùa xuân")
elif month >= 4 and month <= 6:
    print("Bạn sinh vào Mùa hạ")
elif month >= 7 and month <= 9:
    print("Bạn sinh vào Mùa thu")
elif month >= 10 and month <= 12:
    print("Thêm sinh vào Mùa đồng")
else:
    print("Tháng sinh nhập không đúng")

#Trang 34
print("#Trang 34")
print("#Bài 9")

while True:
    num = int(input("Nhập vào bảng cửu chương muốn hiển thị [1-10]: "))
    if 1<=num<=10:
        print("Bảng cửu chương", num)
        for j in range(1,11):
            print(num, 'x', j, '=', num*j)
        break
    else:
        print("Nhập sai, Vui lòng nhập số từ 1 đến 10")
   
#Trang 35
print("#Trang 35")
print("#Bài 10")


def diem_chu(diem):
    if 9.0 <= diem <= 10.0:
        return 'A+'
    elif 8.5 <= diem <= 8.9:
        return 'A'
    elif 8.0 <= diem <= 8.4:
        return 'B+'
    elif 7.0 <= diem <= 7.9:
        return 'B'
    elif 6.5 <= diem <= 6.9:
        return 'C+'
    elif 5.5 <= diem <= 6.4:
        return 'C'
    elif 5.0 <= diem <= 5.4:
        return 'D+'
    elif 4.0 <= diem <= 4.9:
        return 'D'
    else:
        return 'F'
    
def diem_he_4(diem):
    if 9.0 <= diem <= 10.0:
        return 4.0
    elif 8.5 <= diem <= 8.9:
        return 3.7
    elif 8.0 <= diem <= 8.4:
        return 3.5
    elif 7.0 <= diem <= 7.9:
        return 3.0
    elif 6.5 <= diem <= 6.9:
        return 2.5
    elif 5.5 <= diem <= 6.4:
        return 2.0
    elif 5.0 <= diem <= 5.4:
        return 1.5
    elif 4.0 <= diem <= 4.9:
        return 1.0
    else:
        return 0.0

while True:
    diem_he_10 = list(map(float, input("Nhập 9 điểm hệ 10, cách nhau bằng dấu cách: ").split()))

    if len(diem_he_10) != 9:
        print("Vui lòng nhập đúng 9 điểm!")
    else:
        diem_chu_tuong_ung = [diem_chu(diem) for diem in diem_he_10]
        tong_mon_hoc = len(diem_he_10)
        dtb_he_10 = sum(diem_he_10) / tong_mon_hoc
        dtb_he_4 = sum([diem_he_4(diem) for diem in diem_he_10]) / tong_mon_hoc
       
        print("Điểm hệ 10:", diem_he_10)
        print("Điểm chữ tương ứng:", diem_chu_tuong_ung)
        print("---------Điểm Trung Bình---------")
        print("Tổng số môn học:", tong_mon_hoc)
        print("DTB hệ 10:", dtb_he_10)
        print("DTB hệ 4:", dtb_he_4)
        break

#Trang 36
print("#Trang 36")
print("#Bài 11")
print("Kiểm tra số nguyên tố")
def kiem_tra_nguyen_to(n):
    if n <= 1:
        return False 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 
try:
    n = int(input("Nhập vào một số nguyên dương N (N > 1): "))
    if kiem_tra_nguyen_to(n):
        print(f"Số {n} là số nguyên tố!")
    else:
        print(f"Số {n} không phải là số nguyên tố!")
except ValueError:
    print("Vui lòng nhập số nguyên dương.")

#Trang 37
print("#Trang 37")
print("#Bài 12")

def kiem_tra_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def so_nguyen_to_tu_1_den_n(n):
    print("Các số nguyên tố từ 1 tới", n, ":")
    for i in range(2, n + 1):
        if kiem_tra_nguyen_to(i):
            print(i, end=" ")

if __name__ == "__main__":
    n = int(input("Nhập vào một số nguyên dương N (N>1): "))
    so_nguyen_to_tu_1_den_n(n)

#Trang 38
print("#Trang 38")
print("#Bài 13")
def he_10_sang_he_2(n):

  nhiphan = ""
  while n > 0:
    nhiphan = str(n % 2) +nhiphan
    n //= 2
  return nhiphan

num = int(input("Nhập một số nguyên dương: "))

ketqua = he_10_sang_he_2(num)
print(f"{num} (hệ 10) = {ketqua} (hệ 2)")

#Trang 39
print("#Trang 39")
print("#Bài 14")

def tinh_toan_chieu_cao():
    so_luong_sinh_vien = int(input("Nhập số lượng sinh viên: "))
    chieu_cao_str = input("Nhập chiều cao của các sinh viên (cách nhau bởi dấu cách): ")
    chieu_cao = chieu_cao_str.split(' ')

    while len(chieu_cao) != so_luong_sinh_vien:
        print("Số lượng chiều cao không hợp lệ. Vui lòng nhập lại!")
        chieu_cao_str = input("Nhập chiều cao của các sinh viên (cách nhau bởi dấu cách): ")
        chieu_cao = chieu_cao_str.split(' ')
        chieu_cao = [float(cao) for cao in chieu_cao]

        chieu_cao_cao_nhat = max(chieu_cao)
        chieu_cao_thap_nhat = min(chieu_cao)
        chieu_cao_trung_binh = sum(chieu_cao) / len(chieu_cao)
        so_luong_sinh_vien_cao_hon_tb = sum(1 for cao in chieu_cao if cao >= chieu_cao_trung_binh)
        print("Chiều cao cao nhất:", chieu_cao_cao_nhat, "m")

        print("Chiều cao thấp nhất:", chieu_cao_thap_nhat, "m")

        print("Chiều cao trung bình:", chieu_cao_trung_binh, "m")

        print("Số lượng sinh viên có chiều cao >= chiều cao trung bình:", so_luong_sinh_vien_cao_hon_tb)
tinh_toan_chieu_cao()