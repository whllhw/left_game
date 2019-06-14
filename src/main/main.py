# coding:utf-8
import sys
import tkinter as tk

import numpy as np

from src.main import config, util
from src.main.Application import Application
from src.main.controller import CellController
from src.main.matrix_iteration import matrix_iteration
from src.main.model import CellModel
from src.main.state import GameState
from src.main.view import CellView

"""
主函数调用Controller
组装Model View
"""


class GameController:
    """
    游戏控制器
    """

    def __init__(self, handle: Application, cell_model: CellModel, cell_controller: CellController, task_func: list):
        """
        :param handle: 句柄
        :param cell_model 细胞模型
        :param cell_controller 细胞控制器
        :param task_func: 帧更新执行的任务函数
        """
        self.handle = handle
        self._bind_event()
        self.game_state: GameState = GameState.INIT
        # 记录运行中的任务id
        self.task_id = 0
        self.task_func = task_func
        self.cell_model = cell_model
        self.cell_controller = cell_controller
        self.cell_controller.update_view()

    def _bind_event(self):
        """
        为控件添加点击事件
        """
        self.handle.clear_button.bind('<Button-1>', self.clear)
        self.handle.start_or_pause_button.bind('<Button-1>', self.start_or_pause)
        self.handle.canvas.bind('<B1-Motion>', self.mouse_event_add)
        self.handle.canvas.bind('<B3-Motion>', self.mouse_event_delete)
        self.handle.canvas.bind('<Button-1>', self.mouse_event_add)
        self.handle.canvas.bind('<Button-3>', self.mouse_event_delete)

    def start_or_pause(self, event):
        """
        根据当前的状态决定开始还是暂停游戏
        """
        # 开始游戏
        if self.game_state == GameState.PAUSE or self.game_state == GameState.INIT:
            self.game_state = GameState.RUNNING
            self.handle.start_or_pause_button['text'] = 'pause'
            self.run()
        else:
            # 暂停游戏
            self.game_state = GameState.PAUSE
            self.handle.start_or_pause_button['text'] = 'start'
            if self.task_id:
                self.handle.master.after_cancel(self.task_id)
                self.task_id = 0

    def clear(self, event):
        """
        清除canvas上的内容
        """
        self.cell_model.set_cells(np.zeros_like(self.cell_model.get_cells()))
        self.cell_controller.update_view()

    def _mouse_event0(self, event, delete=False):
        if self.game_state == GameState.RUNNING:
            return
        if event.x < 0 or event.y < 0:
            return
        if event.x >= config.config.cnf['width'] or event.y >= config.config.cnf['height']:
            return

        i, j = util.get_x_y(event.x, event.y, self.cell_model.get_cells())
        cells = self.cell_model.get_cells()
        cells[i, j] = 1 if not delete else 0
        self.cell_model.set_cells(cells)
        self.cell_controller.update_single_view(i, j)

    def mouse_event_add(self, event):
        self._mouse_event0(event)

    def mouse_event_delete(self, event):
        self._mouse_event0(event, delete=True)

    def run(self):
        for func in self.task_func:
            func()
        print(config.config.time_frame)
        self.task_id = self.handle.master.after(config.config.time_frame, self.run)

    def main_loop(self):
        self.handle.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry(config.config.wm_geometry)
    root.protocol('WM_DELETE_WINDOW', lambda: sys.exit(0))
    handle = Application(master=root)

    cells = CellModel.init_cells(src_cells=np.random.randint(0, 1, config.config.cell_size))
    view = CellView(handle)

    controller = CellController(cells, view)
    # 构造GameController时，传入每帧执行的函数
    gameController = GameController(handle, cells, controller, [
        lambda: cells.set_cells(matrix_iteration(cells.get_cells())),
        controller.update_view
    ])

    gameController.main_loop()
