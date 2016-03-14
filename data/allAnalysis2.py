import os,sys
import csv

def readCSV(filename):
    data = []
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        data = map(lambda row: (''.join(row)).split(','), spamreader)
    print filename + " Reading Done!"
    return data[0], data[1:]

def writeCSV(filename, titles, delay, flights):
    writer = open(filename,'w')
    writer.write(','.join(titles) + '\n')
    for i, row in enumerate(delay):
        writer.write(', '.join(row[0]) + ',' + str(row[-1])+ ',' + str(flights[i][-1])  + '\n')
    writer.close()
    print "Finished writing!"    

if __name__ == "__main__":
    year = sys.argv[1]
    titles, data = readCSV(year + '-all.csv')
    flights, delay = {}, {}
    # 0 month 1 day 2 delay 3 origin 4 destination
    for d in data:
        flights[(d[0],d[1],d[3],d[4])] = flights.get((d[0],d[1],d[3],d[4]), 0) + 1
        delay[(d[0],d[1],d[3],d[4])] = delay.get((d[0],d[1],d[3],d[4]), 0) + 1 if (d[2] != 'NA')and(int(d[2])>0) else 0

    import operator
    writeCSV('../data-all/' + year + '-all.csv', titles[:2]+titles[3:] + ['Delay', 'Flgihts'], 
            sorted(delay.items(), key=operator.itemgetter(0)), sorted(flights.items(), key=operator.itemgetter(0)))

