# coding:utf-8

import tkinter as tk

import numpy as np

from src.main.main import matrix_iteration


class Application(tk.Frame):
    def __init__(self, master=None, init_matrix=None):
        super().__init__(master)
        self.master = master
        self.size = init_matrix.shape
        self.matrix = init_matrix
        self.grid_ids = np.zeros(self.size)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.cnf = {
            "height": 400,
            "width": 400
        }
        self.cancas = tk.Canvas(master=self.master, cnf=self.cnf)
        self.cancas.create_rectangle(1, 1, 400, 400)
        h, w = self.cnf["height"] / self.size[0], self.cnf["width"] / self.size[1]
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                id = self.cancas.create_rectangle(w * i, h * j, w * (i + 1), h * (j + 1), fill="white")
                self.grid_ids[i, j] = id
        self.cancas.pack()

    def flush(self, mat):
        tmp = matrix_iteration(mat)
        flush_mat = tmp != mat
        mat = tmp
        h, w = self.cnf["height"] / self.size[0], self.cnf["width"] / self.size[1]
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                color = "black" if mat[i, j] == 1 else "white"
                if flush_mat[i, j]:
                    self.cancas.delete(self.grid_ids[i, j])
                    self.grid_ids[i, j] = self.cancas.create_rectangle(
                        w * i, h * j, w * (i + 1), h * (j + 1), fill=color)
        self.matrix = mat
        self.cancas.pack()

    def run(self):
        self.flush(self.matrix)
        self.master.after(3, self.run)


root = tk.Tk()
root.geometry("600x600")
mat = np.random.randint(0, 2, [50, 50])

app = Application(master=root, init_matrix=mat)
app.run()
app.mainloop()
