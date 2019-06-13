# coding:utf-8

import unittest

import numpy as np

from src.main.matrix_iteration import matrix_iteration


class AlgTest(unittest.TestCase):

    def test_matrix_iteration(self):
        input = np.array([
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0]])
        excepted = np.array([
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]])
        result = matrix_iteration(input)
        self.assertTrue((excepted == result).all())

    def test_case(self):
        input = np.array([
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 1]])
        excepted = np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]])
        result = matrix_iteration(input)
        self.assertTrue((excepted == result).all())

    def test_case_2(self):
        input = np.array([
            [0, 0, 1],
            [0, 0, 1],
            [1, 0, 1]])
        excepted = np.array([
            [0, 0, 0],
            [0, 0, 1],
            [0, 1, 0]])
        result = matrix_iteration(input)
        self.assertTrue((excepted == result).all())

    def test_case_3(self):
        input = np.array([
            [0, 0, 0, 1],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 1]
        ])
        excepted = np.array([
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0]
        ])
        result = matrix_iteration(input)
        self.assertTrue((result == excepted).all(), print(excepted, result))

    def print(self, expected, output):
        return expected + '\n' + output
