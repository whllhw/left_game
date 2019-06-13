# coding:utf-8
from enum import Enum


class CellState(Enum):
    """细胞状态
    DEAD    死亡
    SURVIVE 存活
    """
    DEAD = 0
    SURVIVE = 1


class GameState(Enum):
    """游戏的状态枚举
    init    初始化
    running 运行中
    pause   暂停中
    stop    停止
    editting 编辑中
    """
    INIT = 0
    RUNNING = 1
    PAUSE = 2
    STOP = 3
    EDITTING = 4
