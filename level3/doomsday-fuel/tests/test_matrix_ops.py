import pytest

import solution as mod  # lol nice name huh
import matrix as matr


def test_mult(random_square_matrix, matrix_equal):
    for di in range(2, 10):
        m = random_square_matrix(di, 0, 10)
        prod = mod._mult(m, m)
        prod2 = matr.matrix_multiply(m, m)
        assert matrix_equal(prod, prod2)


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
    for di in range(2, 11):
        m = random_square_matrix(di, 2, 10)
        # TODO: check determinant != 0
