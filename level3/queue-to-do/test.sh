#!/usr/bin/env bash
# build
rm *.class
javac -classpath .:target/dependency/* -d . Solution.java


java='java -classpath .:target/dependency/* Solution'
python='python3 solution.py'

for i in {1..1000}; do
  s=$((1 + $RANDOM % 1000))
  l=$((1 + $RANDOM % 1000))
  a_j=$($java $s $l)
  a_p=$($python $s $l)

  if [[ "$a1" != "$a2" ]]; then
    echo "s=$s" "l=$l" "j=$a_j" "p=$a_p"
  else
    echo -n .
  fi
done
echo
