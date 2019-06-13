# coding:utf-8
from src.main.controller import CellController
from src.main.model import CellModel
from src.main.view import CellView

"""
主函数调用Controller
"""
if __name__ == '__main__':
    cell = CellModel()

    view = CellView()

    controller = CellController(cell, view)
    controller.update_view()
    controller.set_cell_state(cell.state.SURVIVE)

    controller.update_view()
