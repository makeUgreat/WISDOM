num = int(input())

lsts = [[0]*3 for _ in range(3)]

value = num
for i in range(len(lsts)):
    for j in range(len(lsts[i])):
        
        if i + j >= 2:
            lsts[i][j] = value
            value += 1
            

for lst in lsts:
    print(*lst,sep='')