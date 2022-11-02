rods = int(input())
loss = rods-1
totLength = 0
while rods > 0:
    length = int(input())
    totLength += length
    rods-=1
totLength = totLength-loss
print(totLength)