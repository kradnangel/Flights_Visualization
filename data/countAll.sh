#!/bin/zsh
for x ({1989..2008});
do cut -f2,3,15,17,18 -d, $x.csv > $x-all.csv;
echo "Dealing with ", $x
python allAnalysis.py $x;
done;
