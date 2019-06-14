# coding:utf-8

import numpy as np

from src.main import util
from src.main.Application import Application
from src.main.model import CellModel


class CellView:
    """
    细胞的视图
    细胞数据的可视化
    """

    def __init__(self, handle: Application):
        self.handle = handle
        self.last_cells = None
        self.grid_ids = None

    def show_detail(self, cells: CellModel.cell):
        """
        根据给定的细胞视图更新视图
        :param cells: 给定的细胞视图
        """
        handle = self.handle
        # 当 grid_ids 和 last_cells 和 cells 的形状相同
        # 说明可以复用之前的绘制图形
        if self.grid_ids is not None:
            diff_before = self.last_cells == cells
            self._draw_canvas(handle, cells, diff_before)
        else:
            # 不能复用之前的图形，需要全部重新绘制
            self.grid_ids = np.zeros_like(cells)
            self._draw_canvas(handle, cells)

        self.last_cells = cells.copy()

    def _draw_canvas_x_y(self, handle: Application, x: int, y: int, width: int, height: int, color='white'):
        """
        绘制指定x y位置的cell
        :param handle: 句柄
        :param x: x
        :param y: y
        :param width: 每个矩形的宽度
        :param height: 每个矩形的高度
        :param color: 颜色
        """
        if self.grid_ids[x, y]:
            handle.canvas.itemconfig(self.grid_ids[x, y], fill=color)
            return
        id = handle.canvas.create_rectangle(width * x,
                                            height * y,
                                            width * (x + 1),
                                            height * (y + 1),
                                            fill=color,
                                            outline="white")
        self.grid_ids[x, y] = id

    def _draw_canvas(self, handle: Application, cells: np.array, diff_before: np.array = None):
        """
        绘制cells
        :param handle: 句柄
        :param cells:  绘制的cells内容
        :param diff_before: 若有此参数则会复用之前创建的矩形
        """
        shape = cells.shape
        width, height = util.get_width_height(cells)
        for i in range(shape[0]):
            for j in range(shape[1]):
                # 当diff_before传入为空，或者当前的位置需要更改
                if diff_before is None or diff_before[i, j]:
                    color = "black" if cells[i, j] == 1 else "white"
                    self._draw_canvas_x_y(handle, i, j, width, height, color)
