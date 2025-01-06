#bài 6 xác dịnh nguyên âm hay phụ âm
ky_tu = input("Nhập vào một ký tự chữ cái bất kỳ: ").lower()
if ky_tu.isalpha() and len(ky_tu) == 1:  
    if ky_tu in "aeiou": 
        print(f"Ký tự '{ky_tu}' là nguyên âm.")
    else:
        print(f"Ký tự '{ky_tu}' là phụ âm.")
else:
    print("Vui lòng nhập một ký tự chữ cái hợp lệ.")