import sys

def solution(n):
    n = int(n)
    i = 0
    while n != 1:
        if (n % 2 == 0):
            n /= 2   
        elif (n % 4 == 1 or n == 3):
            n -= 1   
        else: 
            n += 1     
        i += 1
    return i

print(solution(sys.argv[1]))
