n,m = map(int, input().split())
bridges = 0
i = m
z = 1
while i > 0:
    a,b,c = map(int, input().split())
    if a or b == z:
        z = max(a,b)
        bridges+=c
    elif a and b == z and m and c == 1:
        bridges += 1
        break
    elif a and b == z and m and c == 0:
        break
    i-=1
print(bridges)