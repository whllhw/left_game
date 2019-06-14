# coding:utf-8
import sys
import tkinter as tk

import numpy as np

from src.main import config
from src.main.Application import Application
from src.main.controller import CellController, GameController
from src.main.matrix_iteration import matrix_iteration
from src.main.model import CellModel
from src.main.view import CellView

"""
主函数调用Controller
组装Model View
"""
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry(config.config.wm_geometry)
    root.protocol('WM_DELETE_WINDOW', lambda: sys.exit(0))
    handle = Application(master=root)

    cells = CellModel.init_cells(src_cells=np.random.randint(0, 1, config.config.cell_size))
    view = CellView(handle)

    controller = CellController(cells, view)
    controller.update_view()
    # 构造GameController时，传入每帧执行的函数
    gameController = GameController(handle, cells, controller, [
        lambda: cells.set_cells(matrix_iteration(cells.get_cells())),
        controller.update_view
    ])

    gameController.main_loop()
