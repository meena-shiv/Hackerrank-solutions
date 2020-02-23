#matrix to take input in [i][j] form
l2= [[0]*(len(b) + 1) for i in range(len(a) + 1)]
for i in range(3):
    for j in range(3):
        l2[i][j]=input()
