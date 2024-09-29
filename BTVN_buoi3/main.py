import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file diemPython.csv
df = pd.read_csv('diemPython.csv')

# Chuyển dữ liệu thành mảng numpy
in_data = df.to_numpy()

# Tính tổng số sinh viên đi thi
total_students = len(in_data[:, 1])
print('Tổng số sinh viên đi thi:', total_students)

# Tìm lớp có số sinh viên đạt nhiều điểm A nhất
diem_A = df[df['Đánh giá điểm'] == 'A']
diem_A_by_lop = diem_A['Lớp'].value_counts()
lop_max_diem_A = diem_A_by_lop.idxmax()
so_sv_max_diem_A = diem_A_by_lop.max()

print(f'Lớp có số sinh viên đạt nhiều điểm A nhất là {lop_max_diem_A} với {so_sv_max_diem_A} sinh viên đạt điểm A.')

# Lọc dữ liệu theo lớp
df_K15 = df[df['Lớp'] == 'K15']
df_K16 = df[df['Lớp'] == 'K16']

# Đếm số lượng sinh viên theo đánh giá điểm
data_K15 = df_K15['Đánh giá điểm'].value_counts().sort_index()
data_K16 = df_K16['Đánh giá điểm'].value_counts().sort_index()

# Tạo biểu đồ đường
plt.figure(figsize=(12, 6))
plt.plot(data_K15.index, data_K15.values, label='Lớp K15', marker='o')
plt.plot(data_K16.index, data_K16.values, label='Lớp K16', marker='^')

plt.xlabel('Lớp')
plt.ylabel('Số sinh viên đạt điểm')
plt.legend(loc='upper right')
plt.title('Biểu đồ phân bố điểm theo lớp')
plt.grid(True)
plt.show()
