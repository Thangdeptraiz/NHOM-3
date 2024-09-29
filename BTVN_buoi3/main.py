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

# Tìm lớp có số sinh viên đạt nhiều điểm A nhất
diemA = in_data[:, 4]
diemBc = in_data[:, 5]
lops = in_data[:, 1]
max_diemA = diemA.max()
max_diemA_index = np.where(diemA == max_diemA)
print('Lớp có nhiều sinh viên đạt điểm A nhất là {max_diemA_index} với {max_diemA} sinh viên đạt điểm A')

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
