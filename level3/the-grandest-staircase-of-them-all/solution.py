# THE GRANDEST STAIRCASE OF THEM ALL
#
# Build the stairs from *bottom* to *top* ;P

# Works, but n=199 and n=200 takes four minutes!

import sys


def solution(n):
    w = ss6(n, 1, 1, 0)
    return w

def ss6(n, t, start, w):
    if start >= n or n-t <= 0 or n-t <= start:
        return w

    w += 1
    newstart = start + 1
    t += newstart
    w2 = ss6(n, t, newstart, w)
    t -= start
    start += 1
    return ss6(n, t, start, w2)


if __name__ == '__main__':
    print(solution(int(sys.argv[1])))
