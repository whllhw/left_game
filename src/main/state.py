# coding:utf-8
from enum import Enum


class CellState(Enum):
    """细胞状态
    DEAD    死亡
    SURVIVE 存活
    """
    DEAD = 0
    SURVIVE = 1
