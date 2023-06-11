# Doomsday Fuel

# [x] Identify & Set terminals
# [x] Rearrange to have terminals first (standard form)
# [x] Normalize (counts to fractions)
# [x] Split into 4 matrices (get R and Q from which)
# [ ] calculate F
#     [x] I
#     [x] minus
#     [x] mult
#     [x] inverse
# [x] calculate FR
# [x] common denominator
#     [x] gcd of mult nums
#     [x] use that to get lcm of mult nums
# [x] output format

from fractions import Fraction
# foobar actually runs python2 in sandbox
# from fractions import gcd as f_gcd
from math import gcd as f_gcd


def set_terminals(m):
    """Convert row with all 0s to have corresponding cell = 1

    > 0 2 0 3
      0 0 0 0
      1 0 0 7
      0 0 0 0

    to
    > 0 2 0 3
      0 1 0 0
      1 0 0 7
      0 0 0 1

    rows with non-0s untouched
    """
    terms = []
    nonterms = []
    for x in range(len(m)):
        if sum(m[x]) == 0:
            m[x][x] = 1
            terms.append(x)
        else:
            nonterms.append(x)

    return m, terms, nonterms


def reorder(m, order):
    """Put absorbing matrices first

    >    s0 s1 s2 s3
      s0 0  2  0  3
      s1 0  1  0  0
      s2 1  0  0  7
      s3 0  0  0  1

    to
    >    s1 s3 s0 s2
      s1 1  0  0  0
      s3 0  1  0  0
      s0 2  3  0  0
      s2 0  7  1  0

    (where s1,3 put before s0,2)

    `order` = [1, 3, 0, 2]
    """
    new_m = []
    for i in order:
        row = []
        for j in order:
            row.append(m[i][j])
        new_m.append(row)
    return new_m


def normalize(m, nonterms):
    """Only act on non-terminals

    Make everything a fractions.Fraction object

    >    s1 s3 s0 s2
      s1 1  0  0  0
      s3 0  1  0  0
      s0 2  3  0  0
      s2 0  7  1  0

    to
    >    s1  s3   s0  s2
      s1 1   0    0   0
      s3 0   1    0   0
      s0 2/5 3/5  0   0
      s2 0   7/8  1/8 0

    After which, sum of any row = 1
    """
    for x in nonterms:
        den = sum(m[x])  # get denominator
        m[x] = [Fraction(i, den) for i in m[x]]
    return m


def get_RQ(m, terms):
    start_at = len(terms)
    R = []
    # . . . . .
    # . . . . .
    # x x . . .
    # x x . . .
    for i in range(start_at, len(m)):
        row = []
        # same as just range(start_at)
        for j in range(0, start_at):
            row.append(m[i][j])
        R.append(row)

    Q = []
    # . . . . .
    # . . . . .
    # . . x x x
    # . . x x x
    for i in range(start_at, len(m)):
        row = []
        for j in range(start_at, len(m[0])):
            row.append(m[i][j])
        Q.append(row)

    return R, Q


def calc_F(Q):
    I_minus_Q = _minus(_eye(len(Q)), Q)
    F = _inv(I_minus_Q)
    return F


def calc_FR(F, R):
    """F times R"""
    return _mult(F, R)


def final_result(l):
    """l is of type list[Fraction]"""
    dens = [ i.denominator for i in l ]
    product = 1
    sum = 0
    for d in dens:
        product *= d
        sum += d
    lcm = d // _gcd(dens)

    result = []
    for i in l:
        result.append(i.numerator * ( lcm // i.denominator))
    result.append(lcm)
    return result


#################### helper functions ####################

def _gcd(numbers):
    """GCD of more than two numbers"""
    if len(numbers) == 0:
        raise ValueError("blah blah")

    if len(numbers) >= 2:
        n = f_gcd(numbers[0], numbers[1])
        numbers.pop(0)
        numbers.pop(0)
        if len(numbers) == 0:
            return n
        return _gcd([n] + numbers)

    return numbers[0]


def _minus(m, n):
    if len(n) != len(m) or len(n[0]) != len(m[0]):
        raise ValueError("Subtracting matrices of different dimensions")
    result = []
    for i in range(len(n)):
        row = []
        for j in range(len(n)):
            row.append(m[i][j] - n[i][j])
        result.append(row)
    return result


def _inv(m):
    identity = _eye(len(m))
    mc = _copy(m)
    ic = _copy(identity)
    l = len(m)

    for f in range(l):
        # Focused scalers are on diagonal
        scaler = Fraction(1) / mc[f][f]
        for col in range(l):
            # Apply scaler to focus row
            mc[f][col] = mc[f][col] * scaler
            ic[f][col] = ic[f][col] * scaler

        # Row item - focus row * focus col
        # For all rows except focus
        for row in range(l):
            if row == f:  # XXX: Optimisation opportunity
                continue
            rowscaler = mc[row][f]
            for col in range(l):
                mc[row][col] = mc[row][col] - rowscaler * mc[f][col]
                ic[row][col] = ic[row][col] - rowscaler * ic[f][col]

    # TODO: Maybe verify inverted matrix?
    return ic


def _mult(m, n):
    if len(m[0]) != len(n):
        raise ValueError("Number of columns in first matrix must equal to number of rows in second matrix")

    product = []

    # Each row of m
    for mrow_i in range(len(m)):
        product.append([])
        # Each col of n
        for ncol_i in range(len(n[0])):
            ncol = [ i[ncol_i] for i in n ]
            s = 0
            # Each element in the col
            for nrow_i in range(len(ncol)):
                # m col num = n row num
                # Hence using  nrow_i  to select the m col
                s += ncol[nrow_i] * m[mrow_i][nrow_i]
            product[-1].append(s)

    return product


def _copy(m):
    rows = len(m)
    cols = len(m[0])

    mc = []

    for i in range(rows):
        mc.append([])
        for j in range(cols):
            mc[-1].append(m[i][j])

    return mc


def _eye(length):
    eye = []
    for i in range(length):
        row = []
        for j in range(length):
            row.append(1 if i == j else 0)
        eye.append(row)
    return eye


def _print_m(m):
    for i in m:
        for j in i:
            print(f"{str(j):>5}", end=" ")
        print()


################# putting it all together #################

def solution(m):
    m, terms, nonterms = set_terminals(m)
    # print("Set terminals")
    # _print_m(m); print()

    m = normalize(m, nonterms)
    # print("Normalize (count -> fractions)")
    # _print_m(m); print()

    order = terms + nonterms
    # print('\nReorder to: ', order, '\n', sep='')

    m = reorder(m, order)
    # _print_m(m); print()

    R, Q = get_RQ(m, terms)
    # print("Extract R and Q")
    # print("R")
    # _print_m(R); print()
    # print("Q")
    # _print_m(Q); print()

    F = calc_F(Q)
    # print("Calculate F = (I - Q)^-1")
    # _print_m(F); print()

    FR = calc_FR(F, R)
    # print("Calculate FR")
    # _print_m(FR); print()

    # print("Get probabilities of terminals:", terms)
    # print('    ', '  '.join(str(i) for i in FR[0]),
    #       '\n', sep='')

    # print("Common denomenators and final result")
    res = final_result(FR[0])
    return res


if __name__ == '__main__':
    m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    print(solution(m))
