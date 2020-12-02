a = open('input.txt', 'r')
input = a.readlines()
a.close()

validCount = 0
for line in input: 
    line = line.replace('\n', '')
    if line == '' or line == None:
        break
    numbers = line.split(' ')[0]
    minimumCount = int(numbers.split('-')[0])
    maximumCount = int(numbers.split('-')[1])
    characterToMatch = line.split(' ')[1].replace(':', '') 
    body = line.split(' ')[2] 
    charCount = 0
    for char in body: 
        if char == characterToMatch:
            charCount += 1 
    if charCount >= minimumCount and charCount <= maximumCount:
        validCount += 1 
    

print("Valid Passwords: {}".format(validCount))
