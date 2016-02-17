import csv

def readCSV(filename):
    data = []
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        data = map(lambda row: (''.join(row)).split(','), spamreader)
    print filename + " Reading Done!"
    return data[0], data[1:]

titles, data = readCSV('1988.csv')
print len(data)
print titles