import sys


def solution(n):
    n = int(n)
    # no more steps needed when it's already 1
    if n == 1: return 0

    # divide by two if it's even
    if n % 2 == 0:
        n /= 2
    else:
        # +1 if it will be a multiple of 4
        # unless it's 3:  3 -> 2 -> 1
        # better than:    3 -> 4 -> 2 -> 1
        if (n+1) % 4 == 0 and n != 3:
            n += 2
        # -1 otherwise
        n-=1
    # increment by 1
    return 1 + solution(n)


if __name__ == '__main__':
    print(solution(sys.argv[1]))
