a = open('input.txt', 'r')
data = a.readlines()
a.close()


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
        if self.ecl is not None and self.pid is not None and self.eyr is not None and self.hcl is not None and self.byr is not None and self.iyr is not None and self.hgt is not None: 
            return True 
        return False

    def addItem(self, name, item):
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

counter = 1
# Offset 1
for passp in passPorts:
    if passp.isValid():
        counter += 1
print("Valid Passports: ", counter)