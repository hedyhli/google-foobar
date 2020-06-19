def solution(xs):

    if(xs.count(0) == len(xs)):
        return(str(0))
    if(len(xs) == 1 and len([n for n in xs if n < 0]) == 1):
        return(str(xs[0]))
    if(len([n for n in xs if n < 0]) == 1 and xs.count(0) == len(xs)-1):
        return(str(0))
    
    Val = 1
    for i in xs:
        if (i != 0 and i <= 1000):
            Val *= i

    if Val < 0:
        BigNeg = max([n for n in xs if n < 0])
        Val = Val/BigNeg

    return(str(int(Val)))

fifty = []
for i in range(51):
  fifty.append(2)
print(solution(fifty))
