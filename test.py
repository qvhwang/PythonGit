def tinh_toan_chieu_cao():
    so_luong_sinh_vien = int(input("Nhập số lượng sinh viên: "))
    chieu_cao_str = input("Nhập chiều cao của các sinh viên (cách nhau bởi dấu phẩy): ")
    chieu_cao = chieu_cao_str.split(',')

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