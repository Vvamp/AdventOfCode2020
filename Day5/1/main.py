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
for line in data: 
    line = line.replace('\n', '')
    row = line[:-3]
    column = line[-3:]
    rowval = findBinaryNumRow(row)
    colval = findBinaryNumCol(column)
    seatid = rowval*8+colval
    print("Row: ", rowval, " Col: ", colval, " Seat ID: ", seatid)
    seatIds.append(seatid)
    # print("Col: ", findBinaryNumCol(column))
print("Highest seat: ", max(seatIds))