a = open('input.txt', 'r')
data = a.readlines()
a.close()

toCheck = []
x = 0 
y=0
print("Total length: {},{}".format(len(data), len(data[0])))
while y < len(data):
    while x < len(data[x]):
        toCheck.append((x,y))
        x += 3
        y += 1
        if y >= len(data):
            break
        if x > len(data[x])-3:
            x = x % 31
            
numTrees = 0
for coord in toCheck:
    if data[coord[1]][coord[0]] == '#':
        numTrees += 1 
    
print("Trees: ", numTrees)


