first = input()
first = first.split()
hands = int(first[0])
dom = first[1]
cards = hands * 4
sum=0
while cards != 0:
    card = input()
    all = list(card)
    val=0
    if all[1] == dom:
        if all[0] == "A":
            val=11
        if all[0] == "K":
            val=4
        if all[0] == "Q":
            val=3
        if all[0] == "J":
            val=20
        if all[0] == "T":
            val=10
        if all[0] == "9":
            val=14
    else:
        if all[0] == "A":
            val=11
        if all[0] == "K":
            val=4
        if all[0] == "Q":
            val=3
        if all[0] == "J":
            val=2
        if all[0] == "T":
            val=10   
    sum+=val
    cards-=1
print(sum)