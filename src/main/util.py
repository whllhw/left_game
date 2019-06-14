# coding:utf-8
import numpy as np

from src.main import config


def get_x_y(x, y, cells: np.array):
    w, h = get_width_height(cells)
    return int(x // w), int(y // h)


def get_width_height(cells: np.array):
    shape = cells.shape
    return config.config.cnf['width'] / shape[0], config.config.cnf['height'] / shape[1]
