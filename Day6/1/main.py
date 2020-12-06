a = open('input.txt', 'r')
data = a.readlines()
a.close()

allSumCount = 0
currentCount = 0
currentYesses = [] 

for line in data:
    if line == "\n": # If it's only a new line, start a new group next time 
        allSumCount += currentCount
        currentCount = 0 
        currentYesses = [] 
        continue 
    line.replace('\n', '')
    line.replace(' ', '')
    for char in line:
        if char == " " or char == "\n":
            continue
        if char not in currentYesses:
            currentYesses.append(char) 
            currentCount += 1

# If the last line was missed
if currentCount > 0:
    allSumCount += currentCount
    currentCount = 0 
    currentYesses = []
print("All Yes's: ", allSumCount)