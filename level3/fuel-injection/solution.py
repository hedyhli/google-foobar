# input integer n as a string         (num of fuel pellets)
# return steps needed to get to 1     (num of operations)
# possible actions for steps:         (control mechanisms operations)
#   - minus 1
#   - plus 1
#   - divide 2
#
# constraints:
#   - input n is max 309 digits long, min is 1

import math
import sys


def solution(n):
    n = int(n) # number to start with
    s = 0      # steps needed to get to 1 - the return value.

    ############## divide by power of 2 ##############
    # div by 2, as many times as possible
    quotient = n  # this is needed if n=odd to start with
    if n % 2 == 0:
        # Divide n by the largest power of 2, then save the used
        # power, and the resulting quotient.
        # Using reversed(range()) so we try powers of 2 from
        # largest to smallest
        #                                 (     sqrt n  + 2)
        # because range(start, stop), stop is exclusive
        for power in reversed(range(1, int(math.sqrt(n) + 2))):
            if n % (2**power) == 0:
                quotient = int(n / (2**power))
                break
        s += power
        if quotient == 1:
            # the only place where the function returns
            return power
    ############## use +1/-1, then try again ##############
    # this part runs either because:
    #   - n is odd, or
    #   - quotient after dividing by powers of 2 is not 1.
    #
    # make resulting odd as close to a multiple of 4 as possible
    # quotient ALWAYS odd here
    # except when quotient = 3, it's better to go <3 2 1> than <3 4 2 1>
    s += 1
    quotient -= 1
    # actually quotient += 1 (but, also +1 for -=1 outside if-block)
    # if math.log(quotient + 2, 2).is_integer():
    if (quotient+2) % 4 == 0 and (quotient+1) != 3:
        # if quotient + 1 reaches a multiple of 4, using this over
        # quotient-1 (which would be a normal even number), takes
        # less steps to get to 1.
        #
        # BASICALLY: consider getting to mult4 before decrementing
        # to an even number
        quotient += 2
    return s + solution(quotient)


if __name__ == '__main__':
    print(solution(sys.argv[1]))
