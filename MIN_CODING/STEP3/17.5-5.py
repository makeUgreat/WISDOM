bit = list(map(int,input().split()))
vect = [3,5,4,2,6,6,5]

for i in range(len(vect)):

    if bit[i] == 1:
        vect[i] = 7
    else:
        vect[i] = 0


print(*vect,sep='')

    