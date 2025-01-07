print("#Trang 36")
print("#Bài 11")
print("Kiểm tra số nguyên tố")
while True:
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
            break
        else:
            print(f"Số {n} không phải là số nguyên tố!")
            break
    except ValueError:
        print("Vui lòng nhập số nguyên dương.")
        
