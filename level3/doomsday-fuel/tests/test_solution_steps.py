import random

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
    for di in range(2, 11):  # Test one matrix for every dimension 2 to 10
        mtest = random_matrix(di, 0, 10)
        terms = set()  # List of rows that are terminals

        # Random total number of terminal rows
        for _ in range(random.randint(0, di)):
            term_row = random.randint(0, di-1)
            terms.add(term_row)
            mtest[term_row] = [0] * di

        nonterms = [ i for i in range(di) if i not in terms ]

        mtest, test_terms, test_nonterms = sol.set_terminals(mtest)

        assert set(test_terms) == terms
        assert test_nonterms == nonterms

        for term_row in terms:
            test_term_row = [0] * di
            test_term_row[term_row] = 1
            assert test_term_row == mtest[term_row]


@pytest.mark.parametrize("mtest,order,new_m", [
    (
         [[0, 2],
         [0, 1]],

         [1, 0],

         [[1, 0],
          [2, 0]],
    ),
    (
        [[3, 0, 9, 2],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [2, 4, 1, 0]],

        [2, 0, 1, 3],

        [[1, 0, 0, 0],
         [9, 3, 0, 2],
         [0, 0, 1, 0],
         [1, 2, 4, 0]],
    )
])
def test_reorder_preset(mtest, order, new_m, matrix_equal):
    mtest = sol.reorder(mtest, order)
    assert matrix_equal(mtest, new_m)


def test_reorder_random(random_matrix, matrix_equal):
    for di in range(2, 11):
        mtest = random_matrix(di, 0, 10)
        order = list(range(di))
        random.shuffle(order)

        new_m = sol.reorder(mtest, order)
        i = 0
        for o in order:  # To pass, i must be in sync with o
            row = []
            for row_o in order:
                row.append(mtest[o][row_o])

            assert row == new_m[i]

            i += 1


def test_normalize(random_matrix, matrix_equal):
    for di in range(2, 11):
        mtest = random_matrix(di, 0, 10)
        # Make it act on all rows since the check passes for terminals too.
        new_m = sol.normalize(mtest, list(range(di)))
        for row in new_m:
            assert sum(row) == 1


def test_RQ(random_matrix, matrix_equal):
    for di in range(2, 11):
        mtest = random_matrix(di, 0, 10)
        # di-2 so terms is not ALL rows
        l = random.randint(0, di-2)
        R, Q = sol.get_RQ(mtest, list(range(l)))

        i = 0
        for row in range(di-l, di):
            j = 0
            for col in range(l):
                # Test R (left)
                assert mtest[row][col] == R[i][j]
                j += 1

            j = 0
            for col in range(l, di):
                # Test Q (right)
                assert mtest[row][col] == Q[i][j]
                j += 1

            i += 1
    # FIXME
