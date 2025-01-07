#Trang 17
print("#Trang 17")
print("#Bài 15_a")
print("#1) ")
def greeting():
    name = str(input("Nhập tên: "))
    year = int(input("Nhập năm sinh: "))
    return f"Xin chào {name}, bạn sinh năm {year}"
print(greeting())

print("#2) ")

def rabbit_count():
    months = int(input("Nhập số tháng: "))
    if months < 0:
        return "Số tháng phải lớn hơn hoặc bằng 0!"
    rabbit_count = 2 ** months
    return f"Số thỏ sau {months} tháng là {rabbit_count}."

print(rabbit_count())


print("3) ")
def count_mark():
    scores = input("Nhập danh sách điểm (cách nhau bởi dấu phẩy): ")
    scores = [float(score.strip()) for score in scores.split(",")]
    total_students = len(scores)
    failed_students = len([score for score in scores if score < 5])
    return f"Số sinh viên học lại: {failed_students}, Tổng số sinh viên: {total_students}"

print(count_mark())


#Trang 18
print("#Trang 18")
print("#Bài 15_b")
print("4) ")

def bmi_show(height, weight):
    BMI = weight / (height * height)
    if BMI < 18.5:
        ketqua = "Gầy"
    elif BMI > 18.5 and BMI < 24.9:
        ketqua = "Bình thường"
    elif BMI > 25 and BMI < 29.9:
        ketqua = "Thừa cân"
    else:
        ketqua = "Béo phì"
    return f"BMI: {BMI:.2f}. Nhận xét: {ketqua}"
height = float(input("Nhập chieu cao: "))
weight = float(input("Nhập cân nặng: "))
print(bmi_show(height, weight))

print("5) ")

def cal_point():
    scores = list(map(float, input("Nhập danh sách điểm (cách nhau bởi dấu cách): ").split(" ")))
    avg_10 = sum(scores) / len(scores)
    avg_4 = (avg_10 / 10) * 4
    return f"Điểm trung bình hệ 10: {avg_10:.2f}, hệ 4: {avg_4:.2f}"

print(cal_point())

print("6) ")

def list_prime():
    n = int(input("Nhập một số nguyên dương n: "))
    if n < 2:
        return "Không có số nguyên tố nào trong khoảng từ 1 đến n!"

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_numbers = [num for num in range(2, n + 1) if is_prime(num)]
    return f"Các số nguyên tố từ 1 đến {n} là: {prime_numbers}"

print(list_prime())
