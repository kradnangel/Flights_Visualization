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
        writer.write(', '.join(row[0]) + ','  + str(round(row[-1],1)) + '\n')
    writer.close()
    print "Finished writing!"    

if __name__ == "__main__":
    year = sys.argv[1]
    titles, data = readCSV(year + '-data-delay.csv')
    flights, delay = {}, {}
    for d in data:
        flights[(d[0],d[1],d[2],d[4],d[5])] = flights.get((d[0],d[1],d[2],d[4],d[5]), 0) + 1
        delay[(d[0],d[1],d[2],d[4],d[5])] = delay.get((d[0],d[1],d[2],d[4],d[5]), 0) + int(d[3]) if d[3] != 'NA' else 0

    for flight in flights.keys():
        delay[flight] /= 1.0 * flights[flight]
    import operator
    writeCSV('../delay/' + year + '-day-delay.csv', titles[:2]+titles[3:] + ['AverageDelay'], sorted(delay.items(), key=operator.itemgetter(0)))

