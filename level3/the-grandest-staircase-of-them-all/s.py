# THE GRANDEST STAIRCASE OF THEM ALL
#
# Build the stairs from *bottom* to *top* ;P

# Works, but n=199 and n=200 takes four minutes!

import sys


cache = {}

# def mem(func):
#     def wrapper(n, t, start, w):
#         print(n, t, start, w)
#         if f"{n},{start}" in cache.keys():
#             return w + cache[f"{n},{start}"]
#         w = ss6(n, t, start, w)
#         cache[f"{n},{start}"] = w
#         return w
#     return wrapper


def solution(n):
    w = ss6(n, 1, 1, 0)
    return w


# @mem
def ss6(n, t, start, w):
    # print(cache)
    # if f"{n-t},{start}" in cache.keys():
    #     return w + cache[f"{n-t},{start}"]

    if start >= n or n-t <= 0 or n-t <= start:
        cache[f"{n-t},{start}"] = w
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
