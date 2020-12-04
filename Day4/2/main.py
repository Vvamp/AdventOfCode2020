a = open('input.txt', 'r')
data = a.readlines()
a.close()

import re

class passport():
    def __init__(self, ecl=None, pid=None, eyr=None, hcl=None, byr=None, iyr=None, cid=None, hgt=None, identifier=0):
        self.ecl = ecl 
        self.pid = pid
        self.eyr = eyr 
        self.hcl = hcl 
        self.byr = byr 
        self.iyr = iyr 
        self.cid = cid 
        self.hgt = hgt 
        self.identifier = identifier
    def isValid(self):
        if self.ecl == None or self.pid == None or self.eyr == None or self.hcl == None or self.byr == None or self.iyr == None or self.hgt == None: 
            return False
        currentlyValid = True 
        hairPattern = re.compile("#([a-f0-9]){6}")
        eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        pidPattern = re.compile("[0-9]{9}")
        pidCheck = pidPattern.match(self.pid)
        if len(self.byr) != 4 or int(self.byr) < 1920 or int(self.byr) > 2002:
            currentlyValid = False 
        elif len(self.iyr) != 4 or int(self.iyr) < 2010 or int(self.iyr) > 2020:
            currentlyValid = False 
        elif len(self.eyr) != 4 or int(self.eyr) < 2020 or int(self.eyr) > 2030:
            currentlyValid = False 
        elif self.hgt[-2:] != "cm" and self.hgt[-2:] != "in":
            currentlyValid = False 
        elif hairPattern.match(str(self.hcl)) == None:
            currentlyValid = False
        elif self.ecl not in eyeColors:
            currentlyValid = False
        elif len(self.pid) != 9 or pidCheck == None:
            currentlyValid = False 
        
        return currentlyValid

    def addItem(self, name, item):
        item = item.replace('\n', '')
        if name == "ecl":
            self.ecl = item
        elif name == "pid": 
            self.pid = item 
        elif name == "eyr": 
            self.eyr = item 
        elif name == "hcl": 
            self.hcl = item 
        elif name == "iyr": 
            self.iyr = item 
        elif name == "cid": 
            self.cid = item 
        elif name == "hgt": 
            self.hgt = item 
        elif name == "byr":
            self.byr = item
        else:
            print("ERROR FINDING NAME ")

passPorts = []
currentPassPort = None
passps = 1
cp = []
for line in data: 
    if line == '\n':
        for keydatapair in currentPassPort:
            cp.append((keydatapair.split(':')[0], keydatapair.split(':')[1]))
        currentPassPort = None 
        # newPP = passport(cp['ecl'], cp['pid'], cp['eyr'], cp['hcl'], cp['byr'], bc['iyr', bc['cid'], bc['hgt']])
        newPP = passport(identifier=passps)
        passps += 1
        for keydatapair in cp: 
            newPP.addItem(keydatapair[0], keydatapair[1])
        passPorts = passPorts + [newPP]
        cp = []
        continue 
    if currentPassPort == None: 
        currentPassPort = line.split(' ')
    else:
        currentPassPort = currentPassPort + line.split(' ')

counter = -1
# Offset -1
for passp in passPorts:
    if passp.isValid():
        counter += 1
print("Valid Passports: ", counter)