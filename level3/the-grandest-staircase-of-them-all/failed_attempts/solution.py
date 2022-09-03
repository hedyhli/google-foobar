import sys


def solution(n):
    return s(0, n, 0)


def make(n, left):
    print("make", n, left)
    if left == 0:
        return True
    if left == 1 and n > 1:
        return True
    if left == 2 and n > 2:
        return True

    if n == 2 == left:
        return False
    if n == 3 == left:
        # 3, 2, 1
        return None

    if n <= 3 and left >= 3:
        return False

    # FIXME: too many special cases
    if n == 3 and left == 4:
        return False

    print("split", n, left)
    return None  # Can split more


def s(outer, n, ways):
    if n == 3:
        return 1 + ways

    for i in reversed(range(n//2-1, n)):
        if outer != 0 and outer <= i:
            print("outer", outer)
            continue

        m = make(i, n-i)
        if m:
            ways += 1
            print(i)
        elif m is None:
            if i > n-i:
                ways += 1
                print(i)
            print("recursion", n, i, n-i)
            ways = s(i, n-i, ways)
        elif not m:
            continue

    return ways


if __name__ == '__main__':
    print(solution(int(sys.argv[1])))
