# coding:utf-8
import numpy as np

from src.main import state, config
from src.main.Application import Application
from src.main.config import Config
from src.main.model import CellModel
from src.main.state import GameState
from src.main.view import CellView


class CellController:
    """
    细胞的控制器
    控制数据流向模型对象，在数据变化时更新视图
    """

    def __init__(self, model: CellModel, view: CellView):
        self.model = model
        self.view = view

    def set_cell_state(self, state: state.CellState):
        self.model.state = state

    def get_cell_state(self):
        return self.model.state

    def update_view(self):
        self.view.show_detail(self.model.get_cell())

    def set_cell(self, new_cell: np.array):
        self.model.set_cell(new_cell)

    def get_cell(self) -> CellModel.cell:
        return self.model.get_cell()


class GameController:
    """
    游戏控制器
    """

    def __init__(self, handle: Application, task_func: list):
        """

        :param handle: 句柄
        :param task_func: 帧更新执行的任务函数
        """
        self.handle = handle
        self._bind_event()
        self.game_state: GameState = GameState.INIT
        # 记录运行中的任务id
        self.task_id = 0
        self.task_func = task_func

    def _bind_event(self):
        """
        为控件添加点击事件
        """
        self.handle.clear_button.bind('<Button-1>', self.clear)
        self.handle.start_or_pause_button.bind('<Button-1>', self.start_or_pause)
        self.handle.edit_button.bind('<Button-1>', self.edit)

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
        pass

    def edit(self, event):
        """
        编辑canvas
        """
        pass

    def run(self):
        for func in self.task_func:
            func()
        print(config.Config.time_frame)
        self.task_id = self.handle.master.after(config.Config.time_frame, self.run)

    def main_loop(self):
        self.handle.mainloop()
