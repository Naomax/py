file = "result"
file2 = "result2"

fi = open(file, "r")
fo = open(file2, "w")
maxInf = 999
text = []
cellList = []
for row in fi:
    text.append(row.replace("\n","").split(","))

optItem = 4 # 2:lkg, 3:delay, 4:pPower, 5:nPower
max = maxInf
adr = 0
preadr = 0
for i in range(len(text)):
    if text[i][0] == "" :
        max = maxInf
        if preadr == adr :
            continue
        if len(cellList) == 0:
            continue
        fo.write(key+","+text[adr][1]+","+text[adr][2]+","+text[adr][3]+","+text[adr][4])
        fo.write("\n")
        preadr = adr
        continue
    cell = text[i][0]
    if cell[len(cell)-2] == "X":
        key = cell[:len(cell)-2]
    else:
        key = cell
    if key not in cellList :
        cellList.append(key)
    if i == 0:
        continue
    val = float(text[i][optItem])
    if max > val:
        max = val
        adr = i

fi.close()
fo.close()