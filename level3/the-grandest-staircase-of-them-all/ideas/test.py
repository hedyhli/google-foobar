import sys
from typing import Optional

class BoxChar:
    mid = "├"
    last = "└"
    vbar = "│"
    hbar = "─"

def simple_perm(n: int, x: Optional[int] = None, i: Optional[int] = None) -> None:
    if x is None:
        x = n  # essentially x's default kwarg value
    if x == 0:
        print("\n", end="")
        # TODO (lol)
        # if i != n:
        #     print(BoxChar.vbar, end="")
        return

    for i in range(1, n+1):
        if i != 1:
            print(" " * (2*n-2*x), end="")
        print(i, end="")
        if x > 1:
            print(BoxChar.hbar, end="")
        simple_perm(n, x-1, i)

if __name__ == "__main__":
    simple_perm(int(sys.argv[1]))
