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
# Vẽ biểu đồ phân bố điểm A, B+

plt.figure(figsize=(10, 6))
plt.plot(lops, diemA, label="Điểm A", marker='o')
plt.plot(lops, diemBc, label="Điểm B+", marker='^')

plt.xlabel('Lớp')
plt.ylabel('Số sinh viên đạt điểm')
plt.legend()
plt.title('Biểu đồ phân bố điểm A, B+ theo lớp')
plt.grid(True)
plt.xticks(rotation=45)  # Xoay nhãn trục x để dễ đọc hơn
plt.show()
