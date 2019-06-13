# coding:utf-8
import tkinter as tk

import numpy as np

from src.main import config
from src.main.model import CellModel


class CellView:
    """
    细胞的视图
    细胞数据的可视化
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(config.config.wm_geometry)
        self.app = Application(master=self.root, canvas_config=config.config.cnf)
        self.last_cells = None
        self.grid_ids = None

    def show_detail(self, cells: CellModel.cell):
        """
        根据给定的细胞视图更新视图
        :param cells: 给定的细胞视图
        """
        handle = self.app.get_handle()
        # 当 grid_ids 和 last_cells 和 cells 的形状相同
        # 说明可以复用之前的绘制图形
        if self.grid_ids and self.grid_ids.shape == cells.shape \
                and self.last_cells.shape == cells.shape:
            diff_before = self.last_cells == cells
            self._draw_canvas(handle, cells, diff_before)
        else:
            # 不能复用之前的图形，需要全部重新绘制
            self.grid_ids = np.zeros_like(cells)
            self._draw_canvas(handle, cells)

        self.last_cells = cells

    def _draw_canvas_x_y(self, handle, x, y, width, height, color='white'):
        """
        绘制指定xy位置的cell
        :param handle: 句柄
        :param x: x
        :param y: y
        :param width: 每个矩形的宽度
        :param height: 每个矩形的高度
        :param color: 颜色
        """
        if self.grid_ids[x, y]:
            handle.canvas.delete(self.grid_ids[x, y])
        id = handle.canvas.create_rectangle(width * x,
                                            height * y,
                                            width * (x + 1),
                                            height * (y + 1),
                                            fill=color,
                                            outline="white")
        self.grid_ids[x, y] = id

    def _draw_canvas(self, handle, cells: np.array, diff_before: np.array = None):
        """
        绘制cells
        :param handle: 句柄
        :param cells:  绘制的cells内容
        :param diff_before: 若有此参数则会复用之前创建的矩形
        """
        shape = cells.shape
        height = config.config.cnf['height'] / shape[0]
        width = config.config.cnf['weight'] / shape[1]
        for i in range(shape[0]):
            for j in range(shape[1]):
                if not diff_before or diff_before[i, j]:
                    color = "black" if cells[i, j] == 1 else "white"
                    self._draw_canvas_x_y(handle, i, j, width, height, color)


class Application(tk.Frame):
    """
    创建窗体及绘制UI
    """

    def __init__(self, master=None, canvas_config=None):
        super().__init__(master)
        self.master = master
        self.canvas_config = canvas_config
        self.create_widgets()

    def create_widgets(self):
        """
        创建UI控件
        """
        self.pause_or_start_button = tk.Button(self, text='start')
        self.clear_button = tk.Button(self, text='clear')
        self.canvas = tk.Canvas(master=self.master, cnf=self.canvas_config)
        self.canvas.create_rectangle(1, 1,
                                     self.canvas_config['wight'],
                                     self.canvas_config['height'],
                                     fill="white",
                                     outline="white")
        self.pause_or_start_button.pack()
        self.clear_button.pack()
        self.canvas.pack()

    def get_handle(self):
        return self
