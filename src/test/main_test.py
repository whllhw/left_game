# coding:utf-8

import pytest

import numpy as np

from src.main.matrix_iteration import matrix_iteration

test_inputs = [
    [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ],
    [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ],
    [
        [0, 0, 1],
        [0, 0, 1],
        [1, 0, 1]
    ],
    [
        [0, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 1]
    ]
]
expecteds = [
    [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ],
    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ],
    [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0]
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0]
    ]

]

test_data = list(map(lambda i: (np.array(i[0]), np.array(i[1])), zip(test_inputs, expecteds)))


@pytest.mark.parametrize("test_input,expected", test_data)
def test_matrix_iteration(test_input, expected):
    current = matrix_iteration(test_input)
    assert (expected == current).all() == True
