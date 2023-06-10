from random import randint

import pytest


def generate_random_matrix(di, min, max):
    m = []
    for _ in range(di):
        m.append([])
        for _ in range(di):
            m[-1].append(randint(min, max))
    return m

# TODO: define own helper funcs in matrix.py


@pytest.fixture
def random_matrix():
    return generate_random_matrix
