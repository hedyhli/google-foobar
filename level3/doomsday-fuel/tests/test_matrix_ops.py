import pytest

import solution as mod  # lol nice name huh
import matrix as matr


def test_mult(random_square_matrix, matrix_equal):
    for di in range(2, 10):
        m = random_square_matrix(di, 0, 10)
        prod = mod._mult(m, m)
        prod2 = matr.matrix_multiply(m, m)
        assert matrix_equal(prod, prod2)


def test_det(random_square_matrix):
    for di in range(2, 8):
        m = random_square_matrix(di, 0, 10)
        d1 = matr.determinant(m)
        d2 = mod._det(m)
        assert d1 == d2


@pytest.mark.parametrize("m", [
    [
        [0.6, 0.5],
        [0.3, 1],
    ],
    [
        [1, 0],
        [0, 1],
    ],
    [
        [5, 3, 1],
        [3, 9, 4],
        [1, 3, 5],
    ],
])
def test_inv(m, matrix_equal):
    print(m)
    res = mod._inv(m)
    res2 = matr.invert_matrix(m)
    assert matrix_equal(res, res2)


def test_mult_inv_random_square(random_square_matrix, matrix_equal):
    """Test that a matrix multiplied by its inverse equares the identity matrix"""
    for di in range(2, 8):
        m = random_square_matrix(di, 2, 10)
        # TODO: check determinant != 0
        if mod._det(m) == 0:
            continue

        inv = mod._inv(m)
        prod = mod._mult(inv, m)
        assert matrix_equal(prod, mod._eye(di))


def test_copy(random_matrix, matrix_equal):
    for rows in range(2, 11):
        for cols in range(2, 11):
            m = random_matrix(rows, cols, 0, 10)
            assert matrix_equal(mod._copy(m), m)


def test_eye():
    for di in range(2, 8):
        eye = mod._eye(di)
        for i in range(di):
            assert eye[i] == [0]*i + [1] + [0]*(di-i-1)
