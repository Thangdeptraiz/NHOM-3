import tkinter as tk
from tkinter import messagebox
import numpy as np

class EquationSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Giải hệ phương trình")

        # Số lượng phương trình
        self.n = tk.IntVar(value=2)  # Giá trị mặc định là 2
        self.m = tk.IntVar(value=2)  # Số ẩn, mặc định là 2

        # Nhập số lượng phương trình và ẩn
        self.label_n = tk.Label(root, text="Số lượng phương trình:")
        self.label_n.grid(row=0, column=0)
        self.entry_n = tk.Entry(root, textvariable=self.n, width=5)
        self.entry_n.grid(row=0, column=1)

        self.label_m = tk.Label(root, text="Số lượng ẩn:")
        self.label_m.grid(row=0, column=2)
        self.entry_m = tk.Entry(root, textvariable=self.m, width=5)
        self.entry_m.grid(row=0, column=3)

        self.button_create = tk.Button(root, text="Tạo ô nhập", command=self.create_input_fields)
        self.button_create.grid(row=0, column=4)

        self.input_fields = []  # Danh sách chứa các ô nhập

    def create_input_fields(self):
        # Xóa các ô nhập cũ nếu có
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) > 1:
                widget.grid_forget()

        self.input_fields.clear()

        # Tạo ô nhập cho n phương trình
        for i in range(self.n.get()):
            label = tk.Label(self.root, text=f"Phương trình {i+1}:")
            label.grid(row=i+1, column=0)

            coefficients = []
            for j in range(self.m.get()):
                entry = tk.Entry(self.root, width=5)
                entry.grid(row=i+1, column=j+1)
                coefficients.append(entry)

                if j < self.m.get() - 1:
                    tk.Label(self.root, text=" + ").grid(row=i+1, column=j+2)

            # Ô kết quả c có thể nhập số
            entry_c = tk.Entry(self.root, width=5)
            entry_c.grid(row=i+1, column=self.m.get() + 1)

            # Đặt dấu "=" trước ô nhập cuối cùng
            tk.Label(self.root, text=" = ").grid(row=i+1, column=self.m.get() + 2)

            coefficients.append(entry_c)
            self.input_fields.append(coefficients)

        # Nút bấm để giải hệ phương trình
        self.solve_button = tk.Button(self.root, text="Giải", command=self.solve_equations)
        self.solve_button.grid(row=self.n.get() + 1, column=0, columnspan=self.m.get() + 3)

        # Nhãn hiển thị kết quả
        self.result_label = tk.Label(self.root, text="Kết quả:")
        self.result_label.grid(row=self.n.get() + 2, column=0, columnspan=self.m.get() + 3)

    def solve_equations(self):
        try:
            A = []
            B = []

            for coefficients in self.input_fields:
                row = [float(entry.get()) for entry in coefficients[:-1]]  # Hệ số
                c = float(coefficients[-1].get())  # Kết quả
                A.append(row)
                B.append(c)

            A = np.array(A)
            B = np.array(B)

            det = np.linalg.det(A)

            if det == 0:
                if np.allclose(np.dot(A, [0] * A.shape[1]), B):
                    self.result_label.config(text="Hệ phương trình có vô số nghiệm.")
                else:
                    self.result_label.config(text="Hệ phương trình vô nghiệm.")
            else:
                solution = np.linalg.solve(A, B)
                result_text = ', '.join([f"x{i+1} = {solution[i]:.2f}" for i in range(len(solution))])
                self.result_label.config(text=result_text)

        except Exception as e:
            messagebox.showerror("Error", f"Không thể giải được hệ phương trình: {e}")

# Tạo cửa sổ ứng dụng
root = tk.Tk()
app = EquationSolverApp(root)
root.mainloop()
