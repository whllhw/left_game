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
"""

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry(config.config.wm_geometry)
    root.protocol('WM_DELETE_WINDOW', lambda: sys.exit(0))
    handle = Application(master=root, canvas_config=config.config.cnf)

    cell = CellModel.init_cell(src_cell=np.random.randint(0, 2, [100, 100]))
    view = CellView(handle)

    controller = CellController(cell, view)
    gameController = GameController(handle, [
        lambda: cell.set_cell(matrix_iteration(cell.get_cell())),
        controller.update_view
    ])
    gameController.main_loop()
