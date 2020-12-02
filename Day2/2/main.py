a = open('input.txt', 'r')
input = a.readlines()
a.close()

validCount = 0
for line in input: 
    line = line.replace('\n', '')
    if line == '' or line == None:
        break
    numbers = line.split(' ')[0]
    firstNumIndex = int(numbers.split('-')[0])-1 # +1 because index 0 is 1
    secondNumIndex = int(numbers.split('-')[1])-1 
    characterToMatch = line.split(' ')[1].replace(':', '') 
    body = line.split(' ')[2]
    
    first = False
    second = False 
    if characterToMatch == body[firstNumIndex]:
        first = True 
    if characterToMatch == body[secondNumIndex]:
        second= True 

    if first != second: 
        validCount += 1
print("Valid Passwords: {}".format(validCount))
