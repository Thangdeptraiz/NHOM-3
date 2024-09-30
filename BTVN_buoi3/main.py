import pandas as pd
from numpy import array
import numpy as np
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file diemPython.csv
df = pd.read_csv('diemPython.csv')

# Chuyển dữ liệu thành mảng numpy
in_data = array(df.iloc[:,:])
print(in_data)

# Tính tổng số sinh viên đi thi
total_students = in_data[:, 2]
print('Tổng số sinh viên đi thi:', np.sum(total_students))

# Tìm số lượng sinh viên theo các hạng điểm
diemA = in_data[:, 4]
diemB_plus = in_data[:, 5]
diemB = in_data[:, 6]
diemC_plus = in_data[:, 7]
diemC = in_data[:, 8]
diemD_plus = in_data[:, 9]
diemD = in_data[:, 10]
diemF = in_data[:, 11]


print(f'Số sinh viên đạt điểm A: {np.sum(diemA)}')
print(f'Số sinh viên đạt điểm B+: {np.sum(diemB_plus)}')
print(f'Số sinh viên đạt điểm B: {np.sum(diemB)}')
print(f'Số sinh viên đạt điểm C+: {np.sum(diemC_plus)}')
print(f'Số sinh viên đạt điểm C: {np.sum(diemC)}')
print(f'Số sinh viên đạt điểm D+: {np.sum(diemD_plus)}')
print(f'Số sinh viên đạt điểm D: {np.sum(diemD)}')
print(f'Số sinh viên rớt (F): {np.sum(diemF)}')
# Tính kết quả theo chuẩn đầu ra L1, L2
L1_scores = in_data[:, 12]
L2_scores = in_data[:, 13]

print(f'Trung bình điểm chuẩn đầu ra L1: {np.mean(L1_scores)}')
print(f'Trung bình điểm chuẩn đầu ra L2: {np.mean(L2_scores)}')

# Tìm lớp có nhiều sinh viên đạt điểm A nhất
lops = in_data[:, 1]  # Class identifiers
max_diemA = diemA.max()
max_diemA_index = np.where(diemA == max_diemA)[0]
print(f'Lớp có nhiều sinh viên đạt điểm A nhất là lớp {lops[max_diemA_index]} với {max_diemA} sinh viên đạt điểm A.')

# Vẽ biểu đồ phân bố điểm A, B+, B, C+, C, D+, D, F theo lớp
plt.figure(figsize=(10, 6))
plt.plot(lops, diemA, label="Điểm A", marker='o')
plt.plot(lops, diemB_plus, label="Điểm B+", marker='^')
plt.plot(lops, diemB, label="Điểm B", marker='s')
plt.plot(lops, diemC_plus, label="Điểm C+", marker='d')
plt.plot(lops, diemC, label="Điểm C", marker='x')
plt.plot(lops, diemD_plus, label="Điểm D+", marker='*')
plt.plot(lops, diemD, label="Điểm D", marker='v')
plt.plot(lops, diemF, label="Điểm F", marker='<')

plt.xlabel('Lớp')
plt.ylabel('Số sinh viên đạt điểm')
plt.legend()
plt.title('Biểu đồ phân bố điểm theo lớp')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
#4
# Vẽ biểu đồ cho TX1 và TX2
tx1_scores = in_data[:, 3]  # Cột TX1
tx2_scores = in_data[:, 4]  # Cột TX2

plt.figure(figsize=(10, 6))
plt.plot(lops, tx1_scores, label="Điểm TX1", marker='o')
plt.plot(lops, tx2_scores, label="Điểm TX2", marker='^')

plt.xlabel('Lớp')
plt.ylabel('Điểm bài kiểm tra')
plt.legend()
plt.title('Biểu đồ phân bố điểm TX1 và TX2 theo lớp')
plt.grid(True)
plt.xticks(rotation=45)  # Xoay nhãn trục x để dễ đọc hơn
plt.show()

# Vẽ biểu đồ điểm chuẩn đầu ra L1 và L2 theo lớp
plt.figure(figsize=(8, 5))
plt.plot(lops, L1_scores, label="L1 (Điểm chuẩn đầu ra)", marker='o')
plt.plot(lops, L2_scores, label="L2 (Điểm chuẩn đầu ra)", marker='^')

plt.xlabel('Lớp')
plt.ylabel('Điểm')
plt.legend()
plt.title('Điểm chuẩn đầu ra L1 và L2 theo lớp')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
