import sys
import math

def triangle_base(n: int) -> int:
    """Get highest integer base to fit a triangle number in n"""
    # 1\2(x)(x+1) = n
    # x^2 + x - 2n = 0
    # solve for x then floor it
    x: int = 0
    # ( -b + sqrt b^2 - 4ac ) / 2a
    x = (-1 + math.isqrt(1 + 8*n))//2
    return x
def tri_min(n: int) -> int:
    """Get minimum integer base whose triangle number >= n"""
    # 1\2(x)(x+1) = n
    # x^2 + x - 2n = 0
    # solve for x then floor it
    x: int = 0
    # ( -b + sqrt b^2 - 4ac ) / 2a
    x = math.ceil((-1 + math.sqrt(1 + 8*n))/2)
    return x
def span(x):
    return x - tri_min(x) + 1

def triangle(x: int) -> int:
    """Compute triangle number for x"""
    return (x*x + x)//2

def ways_to_slide(x: int) -> int:
    """Compute number of ways for 2nd step to move bricks to the 1st step \
    and maintain 2nd step > 1st step"""
    return (x-1)//2

def find_slides(a, b, c: int) -> int:
    pass

# def solution(n: int) -> int:
#     max_nsteps: int = triangle_base(n)  # max No of steps on staircase
#     w: int = 0  # number of ways to make the staircase

#     for nsteps in range(1, max_nsteps+1):
#         # for n=7, max_nsteps=3, tri=1+2=3, last_col=7-3=4
#         tri = triangle(nsteps-1)
#         last_col = n - tri
#         w += 1
#         # last_col_diff = 4-2 = 2 (nsteps-1 being 2nd last col)
#         last_col_diff = last_col-nsteps-1
#         if last_col_diff <= 2:
#             continue
#         # first_slide = ways to slide from last to 2nd last col
#         first_slide = ways_to_slide(last_col_diff)
#         w += first_slide
#         if first_slide <= 1 or nsteps <= 2:
#             # - if we can't slide last col for this nsteps, we can't
#             #   slide other cols either. (TODO: OBSOLETE due to last_col_diff)
#             # - if we can slide last col only once, we can't slide
#             #   other cols either. Try 1,2,5 => 1,3,4; 3 can't slide
#             #   to 1.
#             # - no further sliding if there are at most 2 steps for
#             #   this configuration.
#             # This skips higher nsteps (where last_col-nsteps-1 <= 2 SAME TODO)
#             # and lower nsteps (nsteps <= 2).
#             continue

#         # Now we attempt to slide other cols, for this nsteps configuration.
#         # eg: 1,2,7 =>
#         #    1,3,6 [END]
#         #    1,4,5 => 2,3,5 [END]
#         for slide in range(1, first_slide+1)

#     return w


# if __name__ == '__main__':
#     print(solution(int(sys.argv[1])))
