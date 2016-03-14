#!/bin/zsh
for x ({1988..2008});
do 
#cut -f2,3,15,17,18 -d, $x.csv > $x-all.csv;
echo "Dealing with ", $x
python allAnalysis2.py $x;
done;
