#!/usr/bin/env bash

# TODO: test values and test time

python1='python3 solution.py'
python2='python3 s.py'

for i in {1..100}; do
    n=$((2 + $RANDOM % 200))
    p1=$($python1 $n)
    p2=$($python2 $n)

    if [[ "$p1" != "$p2" ]]; then
        echo "n=$n"
        echo "solution.py: $p1"
        echo "s.py: $p2"
    else
        echo -n .
    fi
done
echo
