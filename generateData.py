import random, string

file = "result"
fo = open(file, "w")

cellNumber = 300
cellRange  = 5
areaMax = 50
delayMax = 10
lkgMax = 10
pPower = 10
nPower = 10

def randomName(n):
    randlst = [random.choice(string.ascii_letters + string.digits).upper() for i in range(n)]
    return ''.join(randlst)
fo.write("cell, area, cell leakage, delay, propagation power, non-propagation")
fo.write("\n")
for i in range(cellNumber):
    key=randomName(4)
    area = str(random.random()*areaMax)
    flag = 0
    for j in range(random.randint(1, cellRange)):

        if random.random() > 0.5 and flag == 0:
            print("yes")
            cell = key
            flag = 1
        else :
            cell = key + "X" + str(j+1) 
        fo.write(cell+","+area+","+str(lkgMax*random.random())+","+str(delayMax*random.random())+","+str(pPower*random.random())+","+str(nPower*random.random()))
        fo.write("\n")
    fo.write("\n\n\n")

fo.close()