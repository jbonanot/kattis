X = 0
count = 0
addends = int(input())
while addends > 0:
    num = int(input())
    expo = num % 10
    newNum = num//10
    p = pow(newNum,expo)
    X+=p
    addends-=1
print(X)