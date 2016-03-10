#!/bin/zsh
for x ({1988..2008});
do cut -f1,2,3,15,17,18 -d, $x.csv > $x-data-delay.csv;
echo "Dealing with ", $x
python delayAnalysis.py $x;
done;
