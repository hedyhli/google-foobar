import sys


def solution(n):
    return ss(n, 0, [0], 0)


def ss(n, t, s, w):
    print("ss", n, t, s, w)

    if n == 0 and len(s) == 1:
        return w
    if n < 0:
        return w

    last = s[-1]
    if len(s) == 1 and s[0] == 0:
        s.pop()

    if n == 0:
        w += 1
        print(s)
        last = s.pop()
        t -= last
        n += last
        last = s.pop()
        t -= last
        n += last

    elif t > n and n <= last:
        last = s.pop()
        t -= last
        n += last

    newlast = last+1

    if newlast > (n+t)-1:
        return w

    s.append(newlast)
    w = ss(n-(newlast), t+(newlast), s, w)
    return w


if __name__ == '__main__':
    print(solution(int(sys.argv[1])))
