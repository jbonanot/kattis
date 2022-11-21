i = 0
while True:
    try:
        a,b = map(int, input().split())
        c,d = map(int, input().split())
        det = a*d - b*c
        A = int((1/det)*d)
        B = int((1/det)*-b)
        C = int((1/det)*-c)
        D = int((1/det)*a)
        print("Case {}:".format(i+1))
        print(A,B)
        print(C,D)
        input()
        i+=1
    except EOFError:
        break