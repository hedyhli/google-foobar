# THE GRANDEST STAIRCASE OF THEM ALL
#
# Build the stairs from *bottom* to *top* ;P

# Works, but n=199 and n=200 takes four minutes!

def solution(n):
    w, _ = ss5(n, 1, 1, 0)
    return w

def ss5(n, t, start, w):
    if start >= n or n-t <= 0 or n-t <= start:
        # n += start
        t -= start
        return w, start

    w += 1
    newstart = start + 1
    # n -= start
    t += newstart
    w, oldstart = ss5(n, t, newstart, w)
    if oldstart != 0:
        t -= start
        start += 1
        # t -= start
        return ss5(n, t, start, w)


print(solution(200))
