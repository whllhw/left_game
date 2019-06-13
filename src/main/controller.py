# coding:utf-8
import numpy as np

from src.main import state
from src.main.model import CellModel
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

    def update_view(self, cells: np.array):
        self.view.show_detail(cells)

    def set_cell(self, new_cell: np.array):
        self.model.set_cell(new_cell)

    def get_cell(self):
        return self.model.get_cell()
