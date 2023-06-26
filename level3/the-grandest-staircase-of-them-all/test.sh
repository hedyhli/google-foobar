#!/usr/bin/env bash

# TODO: test values and test time

python1='python3 solution.py'
# python2='python3 s.py'

rm *.class
javac Solution.java
java='java Solution'

for i in {1..100}; do
    n=$((2 + $RANDOM % 100))
    p1=$($python1 $n)
    # p2=$($python2 $n)
    j1=$($java $n)

    if [[ "$p1" != "$j" ]]; then
        echo "n=$n"
        echo "solution.py: $p1"
        echo "java: $j"
        # echo "s.py: $p2"
    else
        echo -n .
    fi
done
echo
