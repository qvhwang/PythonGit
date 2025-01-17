import numpy as np
path = 'dayso1_bai17.txt'
diem_2a = np.loadtxt(path, delimiter = ' ', dtype=np.int32)

print(diem_2a)
for i in range(0,diem_2a.shape[1]):
    print('Điểm trung bình của học sinh ',i, ' : ', diem_2a[:,i].mean())
diemtb = diem_2a.mean(axis = 0)
diem_cao = np.argmax(diemtb)
print('Học sinh có điểm trung bình cao nhất: ', diem_cao, '-- Điểm: ', diemtb[diem_cao])
print('Bảng điểm đầy đủ của học sinh: ', diem_cao, ' : ', diem_2a.T[diem_cao])
diem_thap = np.argmin(diemtb)
print('Học sinh có điểm trung bình thấp nhất ', diem_thap, '-- Điểm: ', diemtb[diem_thap])
print('Bảng điểm đầy đủ của học sinh: ', diem_thap, ' : ', diem_2a.T[diem_thap])