def solution(n, t=1, s=1, w=0):
    if s >= n or n-t <= s:
        return w

    w = solution(n, t+s+1, s+1, w+1)
    return solution(n, t+1, s+1, w)


## THE GRANDEST STAIRCASE OF THEM ALL ##
#
# Build the stairs from *bottom* to *top*.
#
# Works, but n=199 and n=200 takes four minutes!
#
# Solution function can easily be a one liner lmao.
# Amazing for golfing.
#
# t=test, s=start, w = starcase "ways" accumulation for the solution(n)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please provide an integer argument n for solution(n)")
        exit(1)
    print(solution(int(sys.argv[1])))
