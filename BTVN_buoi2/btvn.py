import tkinter as tk
from tkinter import messagebox
import numpy as np

def solve_equation():
    try:
        # Lấy dữ liệu từ các entry
        a1 = float(entry_a1.get())
        b1 = float(entry_b1.get())
        c1 = float(entry_c1.get())
        a2 = float(entry_a2.get())
        b2 = float(entry_b2.get())
        c2 = float(entry_c2.get())

        # Tạo ma trận hệ số
        A = np.array([[a1, b1], [a2, b2]])
        B = np.array([c1, c2])

        # Giải hệ phương trình bằng hàm linalg.solve
        solution = np.linalg.solve(A, B)

        # Hiển thị kết quả
        result_label.config(text=f"x = {solution[0]:.2f}, y = {solution[1]:.2f}")
    except Exception as e:
        messagebox.showerror("Error", f"Không thể giải được hệ phương trình: {e}")

# Tạo cửa sổ ứng dụng
root = tk.Tk()
root.title("Giải hệ phương trình")

# Tạo các nhãn và ô nhập cho phương trình thứ nhất
label_eq1 = tk.Label(root, text="Phương trình 1 (ax + by = c):")
label_eq1.grid(row=0, column=0, columnspan=2)
entry_a1 = tk.Entry(root, width=5)
entry_a1.grid(row=1, column=0)
label_x1 = tk.Label(root, text="x +")
label_x1.grid(row=1, column=1)
entry_b1 = tk.Entry(root, width=5)
entry_b1.grid(row=1, column=2)
label_y1 = tk.Label(root, text="y =")
label_y1.grid(row=1, column=3)
entry_c1 = tk.Entry(root, width=5)
entry_c1.grid(row=1, column=4)

# Tạo các nhãn và ô nhập cho phương trình thứ hai
label_eq2 = tk.Label(root, text="Phương trình 2 (ax + by = c):")
label_eq2.grid(row=2, column=0, columnspan=2)
entry_a2 = tk.Entry(root, width=5)
entry_a2.grid(row=3, column=0)
label_x2 = tk.Label(root, text="x +")
label_x2.grid(row=3, column=1)
entry_b2 = tk.Entry(root, width=5)
entry_b2.grid(row=3, column=2)
label_y2 = tk.Label(root, text="y =")
label_y2.grid(row=3, column=3)
entry_c2 = tk.Entry(root, width=5)
entry_c2.grid(row=3, column=4)

# Nút bấm để giải hệ phương trình
solve_button = tk.Button(root, text="Giải", command=solve_equation)
solve_button.grid(row=4, column=0, columnspan=5)

# Nhãn hiển thị kết quả
result_label = tk.Label(root, text="Kết quả:")
result_label.grid(row=5, column=0, columnspan=5)

# Bắt đầu vòng lặp chính của Tkinter
root.mainloop()
