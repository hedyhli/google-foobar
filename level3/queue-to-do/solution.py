import sys

def solution(start, length):
    ans = start

    for n in range(1, length+1):
        items = -n + length + 1
        first = (n-1) * length + start
        for x in range(first, items+first):
            ans = ans^x

    return ans^start

# print(sys.argv)
print(solution(int(sys.argv[1]), int(sys.argv[2])))
