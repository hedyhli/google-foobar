#!/usr/bin/env bash


python1='python3 solution.py'
python2='python3 s.py'

f1=0
f2=0
for i in {1..100}; do
    n=$((2 + $RANDOM % 200))

    time1=$(date +%6N)
    p1=$($python1 $n)
    time2=$(date +%6N)
    p1_time=$(echo "$time2-$time1"|bc)

    time1=$(date +%6N)
    p2=$($python2 $n)
    time2=$(date +%6N)
    p2_time=$(echo "$time2-$time1"|bc)

    if (( $p1_time < $p2_time )); then
        f1=$((f1+1))
    else
        f2=$((f2+1))
    fi

    if [[ "$p1" != "$p2" ]]; then
        echo "n=$n"
        echo "solution.py: $p1"
        echo "s.py: $p2"
        echo
    else
        echo -n .
    fi
done
echo $f1 $f2
