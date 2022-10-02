file = "result2"
file2 = "ref"

output = "result3"
fi = open(file, "r")
fi2 = open(file2, "r")
fo = open(output, "w")

text = []
text2 = []
for row in fi:
    text.append(row)
for row in fi2:
    text2.append(row)

for i in range(len(text2)):
    for j in range(len(text)):
        if text2[i].split(",")[0] == text[j].split(",")[0]:
            text2[i] = text[j]
            break

for i in range(len(text2)):
    fo.write(text2[i])
fo.close()