m,n = map(int, input().split())
dictionary = {}
jDesc = []
trueDesc = []
totalCash = 0

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
def flatten(l):
    return [item for sublist in l for item in sublist]

while m > 0:
    job, pay = [x for x in input().split()]
    dictionary[job] = pay
    m+=-1

while n > 0:
    while True:
        description = input()
        if description == '.':
            break
        else:
            jDesc.append(description.split())
    trueDesc = flatten(jDesc)
    overlap = intersection(trueDesc, dictionary)
    i = len(overlap) - 1
    while i >= 0:
        pay1 = dictionary[overlap[i]]
        totalCash += int(pay1)
        i+=-1
    print(totalCash)
    n+=-1
    totalCash = 0
    jDesc = []
    trueDesc = []