a = open('input.txt', 'r')
input = a.readlines()
a.close()

goal = 2020
print(input)
for line in input: 
    for line2 in input:
        line = line.replace('\n', '') 
        line2 = line2.replace('\n', '')
        #print("{}, {}".format(line, line2))
        if line == '' or line2 == '':
            continue
#        print("Result: {}".format(int(line) + int(line2)))
        if int(line) + int(line2) == goal: 
            print("RESULT: {} * {} = {}".format(line, line2, int(line)*int(line2)))
            exit(0)
print("No results found. Probabl error in code")
