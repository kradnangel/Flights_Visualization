#!/bin/zsh
for x ({2001..2002});
do cut -f17,18 -d, $x-2.csv > $x-17-18.csv;
python dataAnalysis.py $x;
done;
