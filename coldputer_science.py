line = ''
newLine = ''
line = input()
temps = int(line.split()[0])
newLine = input()
tempur = list(newLine.split())
i=0
negs = 0
for temps in tempur:
    if int(tempur[i]) < 0:
        negs+=1
    i+=1
print(negs)