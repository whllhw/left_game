# coding:utf-8
import numpy as np
from easygui import *

from src.main import config


def get_x_y(x, y, cells: np.array):
    w, h = get_width_height(cells)
    return int(x // w), int(y // h)


def get_width_height(cells: np.array):
    shape = cells.shape
    return config.config.cnf['width'] / shape[0], config.config.cnf['height'] / shape[1]


def save_file(cells: np.array):
    filename = filesavebox(default='map')
    print(cells)
    if filename:
        np.save(filename, cells)


def load_file():
    filename = fileopenbox(default='map')
    if filename:
        return np.load(filename)


if __name__ == '__main__':
    save_file(np.zeros((1, 1)))
    print(load_file())
