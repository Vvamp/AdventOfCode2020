a = open('input.txt', 'r')
input = a.readlines()
a.close()

goal = 2020
print(input)
for line in input: 
    for line2 in input:
        for line3 in input:
            line = line.replace('\n', '') 
            line2 = line2.replace('\n', '')
            line3 = line3.replace('\n', '') 
            if line == '' or line2 == '' or line3 == '':
                continue
#        print("Result: {}".format(int(line) + int(line2)))
            if int(line) + int(line2) + int(line3) == goal: 
                print("RESULT: {} * {} * {} = {}".format(line, line2, line3, int(line)*int(line2)*int(line3)))
                exit(0)
print("No results found. Probabl error in code")
