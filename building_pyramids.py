blocks = int(input(""))
layers = 0
size = 1
up = 3
while blocks >= size:
    blocks = blocks - size
    size = (up)**2
    up = up + 2
    layers = layers + 1
print(layers)