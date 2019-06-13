# coding:utf-8
import numpy as np

from src.main.state import CellState


class CellModel:
    """细胞模型定义
    由于细胞的底层存储就是np数组，
    所以直接使用类的静态方法去存储
    """

    cell: np.array = None

    def __init__(self, state: CellState = CellState.DEAD):
        """
        :param state: 细胞的初始状态
        """
        self.state = state

    def __getstate__(self):
        return self.state

    def __setstate__(self, state: CellState):
        self.state = state

    @classmethod
    def init_cell(cls, x_size: int = 50, y_size: int = 50, src_cell: np.array = None):
        """
        初始化底层数组
        :param x_size: 长
        :param y_size: 宽
        :param src_cell: 原始array，若有则直接拷贝一份
        """
        assert x_size > 0 and y_size > 0
        if src_cell is not None:
            cls.cell = src_cell.copy()
        else:
            cls.cell = np.zeros((x_size, y_size))
        return cls

    @classmethod
    def get_cell(cls):
        if hasattr(cls, 'cell'):
            return cls.cell
        else:
            raise RuntimeError('尚未初始化')

    @classmethod
    def set_cell(cls, new_cell: np.array):
        cls.cell = new_cell
