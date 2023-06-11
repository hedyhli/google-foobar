from random import randint
import typing as T

import pytest


def _random_square_matrix(di, min, max):
    m = []
    for _ in range(di):
        m.append([])
        for _ in range(di):
            m[-1].append(randint(min, max))
    return m


def _random_matrix(rows, cols, min, max):
    m = []
    for _ in range(rows):
        m.append([])
        for _ in range(cols):
            m[-1].append(randint(min, max))
    return m


def _matrix_equal(m1, m2, roundto: T.Optional[int] = None):
    if len(m1) != len(m2):
        return False
    if len(m1) >= 1 and len(m1[0]) != len(m2[0]):
        return False

    for i in range(len(m1)):
        for j in range(len(m1[0])):
            a, b = m1[i][j], m2[i][j]
            if roundto:
                a, b = round(a, roundto), round(b, roundto)
            if a != b:
                return False

    return True


@pytest.fixture
def random_square_matrix():
    return _random_square_matrix

@pytest.fixture
def random_matrix():
    return _random_matrix

@pytest.fixture
def matrix_equal():
    return _matrix_equal
