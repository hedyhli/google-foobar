#!/usr/bin/env bash

# TODO: test values and test time

# python1='python3 solution.py'
python2='python3 s_new.py'
python3='python3 s.py'

for i in {1..100}; do
    n=$((2 + $RANDOM % 200))
    # p1=$($python1 $n)
    p2=$($python2 $n)
    p3=$($python3 $n)

    if [[ "$p2" != "$p3" ]]; then
        echo "n=$n"
        # echo "solution.py: $p1"
        echo "s_new.py: $p2"
        echo "s.py: $p3"
        echo
    else
        echo -n .
    fi
done
echo
