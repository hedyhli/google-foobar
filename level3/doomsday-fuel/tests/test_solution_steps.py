import pytest

import solution as sol
import matrix as matr

@pytest.mark.parametrize("mtest,mresult,terms,nonterms", [
    (
        [[0, 2, 0, 3],
         [0, 0, 0, 0],
         [1, 0, 0, 7],
         [0, 0, 0, 0]],

        [[0, 2, 0, 3],
         [0, 1, 0, 0],
         [1, 0, 0, 7],
         [0, 0, 0, 1]],

        [1, 3],  # Terminal rows
        [0, 2],  # Non-terminal rows
    ),
    (
        [[1, 8],
         [0, 0]],

        [[1, 8],
         [0, 1]],

        [1],
        [0],
    ),
])
def test_terminals_preset(mtest, mresult, terms, nonterms, matrix_equal):
    """Test set_terminals with preset expected results"""
    mtest, test_terms, test_nonterms = sol.set_terminals(mtest)
    assert matrix_equal(mtest, mresult)
    assert test_terms == terms
    assert test_nonterms == nonterms


def test_terminals_random(random_matrix, matrix_equal):
    """Test set_terminals with random matrices as input"""
    # TODO
