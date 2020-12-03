a = open('input.txt', 'r')
data = a.readlines()
a.close()


def checkTrees( goRight=3, goDown=1):
    print("Check trees for: D:{} R:{}".format(goDown, goRight))
    toCheck = []
    x = 0 
    y=0
    while y < len(data):
        while x < len(data[x]):
            toCheck.append((x,y))
            x += goRight
            x = x % 31
            y += goDown
            if y >= len(data):
                break

    numTrees = 0
    for coord in toCheck:
        if data[coord[1]][coord[0]] == '#':
            numTrees += 1 
        
    print("Trees: ", numTrees)
    return numTrees

tt = (checkTrees(1,1) * checkTrees(3, 1) * checkTrees(5, 1) * checkTrees(7,1) * checkTrees(1,2))
print("Total Trees Multiplied: ", tt)


