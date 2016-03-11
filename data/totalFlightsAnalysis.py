import os,sys
import csv

def readCSV(filename):
    data = []
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        data = map(lambda row: (''.join(row)).split(','), spamreader)
    print filename + " Reading Done!"
    return data[0], data[1:]

def writeCSV(filename, titles, content):
    writer = open(filename,'w')
    writer.write(','.join(titles) + '\n')
    for row in content:
        writer.write(row[0] +',' + row[1] +',' + str(content[row]) + '\n')
    writer.close()
    print "Finished writing!"    

if __name__ == "__main__":
    year = sys.argv[1]
    titles, data = readCSV(year + '-flgihts-each-day.csv')
    flights = {}
    for d in data:
        flights[(d[0],d[1],d[2],d[3])] = flights.get((d[0],d[1],d[2],d[3]), 0) + 1

    writeCSV('../data-total-flights/' + year + '-total-flights.csv', titles + ['Total'], flights)

