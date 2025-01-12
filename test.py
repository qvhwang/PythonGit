import numpy as np
path = 'data.txt'
diem_2a = np.loadtxt(path, delimiter = ',', dtype=np.int32)

print(diem_2a)
print('Điểm môm học đầu tiên, của học sinh đầu tiên:', diem_2a[0, 0])
print('Điểm môn học thứ 1, của học sinh thứ 3:', diem_2a[1, 3])
print('Điểm môn học cuối, của học sinh cuối:', diem_2a[-1, -1])
print('----------------------------')
print('Bảng điểm lớp 2A: \n', diem_2a)