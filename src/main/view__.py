# coding:utf-8

import tkinter as tk
import numpy as np
from src.main.matrix_iteration import matrix_iteration


class Application(tk.Frame):
    def __init__(self, master=None, init_matrix=None):
        super().__init__(master)
        self.master = master
        self.size = init_matrix.shape
        self.matrixs = [np.zeros_like(init_matrix), init_matrix]
        self.grid_ids = np.zeros(self.size)
        self.pack()
        self.cnf = {
            "height": 400,
            "width": 400,
        }
        self.config = {
            'delay': 300
        }
        self.h, self.w = self.cnf["height"] / self.size[0], self.cnf["width"] / self.size[1]
        self.create_widgets()
        self.task_id = 0

    def create_widgets(self):
        self.pause_button = tk.Button(self, text="START", command=self.pause)
        self.clear_button = tk.Button(self, text="CLEAR", command=self.clear)
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.clear_button.pack()
        self.pause_button.pack()
        self.quit.pack()
        self.canvas = tk.Canvas(master=self.master, cnf=self.cnf)
        self.canvas.create_rectangle(1, 1, 400, 400, fill="white", outline="white")
        self._draw_canvas()
        self.canvas.pack()

    def _draw_canvas_x_y(self, i, j, color='white'):
        if self.grid_ids[i, j]:
            self.canvas.delete(self.grid_ids[i, j])
        id = self.canvas.create_rectangle(self.w * i, self.h * j, self.w * (i + 1), self.h * (j + 1), fill=color,
                                          outline="white")
        self.grid_ids[i, j] = id

    def _draw_canvas(self):
        flush_mat = self.matrixs[-1] != self.matrixs[-2]
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if flush_mat[i, j]:
                    color = "black" if self.matrixs[-1][i, j] == 1 else "white"
                    self._draw_canvas_x_y(i, j, color)

    def set_matrix(self, mat):
        self.matrixs.pop(0)
        self.matrixs.append(mat)

    def flush(self):
        tmp = matrix_iteration(self.matrixs[-1])
        self.set_matrix(tmp)
        self._draw_canvas()

    def _run(self):
        self.flush()
        self.task_id = self.master.after(self.config['delay'], self._run)

    def start_init(self):
        self.canvas.bind('<B1-Motion>', self.mouse_event)

    def stop_init(self):
        self.canvas.unbind('<B1-Motion>')

    def mouse_event(self, event):
        if event.x < 0 or event.y < 0:
            return
        if event.x >= self.cnf['width'] or event.y >= self.cnf['height']:
            return
        x = int(event.x // self.w)
        y = int(event.y // self.h)
        mat = self.matrixs[-1].copy()
        mat[x, y] = 1
        self.set_matrix(mat)
        self._draw_canvas_x_y(x, y, 'black')

    def pause(self):
        """
        暂停或开始游戏
        :return:
        """
        if self.task_id:
            self.start_init()
            self.master.after_cancel(self.task_id)
            self.task_id = 0
            self.pause_button['text'] = 'START'
        else:
            self.stop_init()
            self.pause_button['text'] = 'PAUSE'
            self._run()

    def clear(self):
        self.set_matrix(np.zeros_like(self.matrixs[-1]))
        self._draw_canvas()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("600x600")
    mat = np.random.randint(0, 2, [10, 10])
    # mat = np.zeros((50, 50))
    app = Application(master=root, init_matrix=mat)
    # app.run()
    app.start_init()
    app.mainloop()
