import numpy as np


def matrix_iteration(mat):
    result = np.zeros_like(mat)
    m, n = mat.shape
    pad_mat = np.zeros((m + 2, n + 2))
    pad_mat[1:m + 1, 1:n + 1] = mat[:, :]
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            tmp = np.sum(pad_mat[i:i + 3, j:j + 3]) - pad_mat[i + 1, j + 1]
            if tmp == 3:
                result[i, j] = 1
            elif tmp == 2:
                result[i, j] = pad_mat[i + 1, j + 1]
            else:
                result[i, j] = 0
    return result


if __name__ == '__main__':
    print(matrix_iteration(np.array([
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ])))
