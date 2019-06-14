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

    def update_view(self):
        self.view.show_detail(self.model.get_cells())

    def update_single_view(self, x: int, y: int):
        self.view.show_i_j(self.model.get_cells(), x, y)

    def set_cell(self, new_cell: np.array):
        self.model.set_cells(new_cell)

    def get_cell(self) -> CellModel.cell:
        return self.model.get_cells()


