import copy 
a = open('input.txt', 'r')
data = a.readlines()
a.close()
import math


def findBinaryNumRow(x):
    value = list(range(128))
    for i in range(len(x)):
        thevalue = len(value)
        dividevalue =  math.ceil(thevalue / 2 )
        if(thevalue == 1):
            break
        if x[i] == 'B':
            value = value[dividevalue:]
        else: 
            value = value[:dividevalue]

    return value[0]

def findBinaryNumCol(x):
    value = list(range(8))
    for i in range(len(x)):
        thevalue = len(value)
        dividevalue =  math.ceil(thevalue / 2 )
        if(thevalue == 1):
            break
        if x[i] == 'R':
            value = value[dividevalue:]
        else: 
            value = value[:dividevalue]

    return value[0]

seatIds = []
rows = [] 
cols = []
for line in data: 
    line = line.replace('\n', '')
    row = line[:-3]
    column = line[-3:]
    rowval = findBinaryNumRow(row)
    colval = findBinaryNumCol(column)
    rows.append(rowval)
    cols.append(colval)
    seatid = rowval*8+colval
    seatIds.append(seatid)
    # print("Col: ", findBinaryNumCol(column))

for i in range(min(seatIds), max(seatIds)):
    for j in range(0, 8):
        potentialMultiple = i-j 
        potentialRow = potentialMultiple/8 
        number_dec = str(potentialRow-int(potentialRow))[1:]
        if number_dec == ".0":
            if i not in seatIds:
                print("Potential Seat ID: ", i)