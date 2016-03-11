#!/bin/zsh
for x ({1988..2008});
do cut -f2,3,17,18 -d, $x.csv > $x-flights-each-day.csv;
echo "Dealing with ", $x
python totalFlightsAnalysis.py $x;
done;
