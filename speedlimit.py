line = ''
while line != '-1':
    miles=0
    speeds=0
    prevTime=0
    line = input()
    num = line.split()
    speeds = int(num[0])
    while speeds > 0:
        line = input()
        num = line.split()
        miles = miles + int(num[0]) * (int(num[1])-int(prevTime))
        prevTime = int(num[1])
        speeds-=1
    if line != '-1':
        print(miles, " miles")  