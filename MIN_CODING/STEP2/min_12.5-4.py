num = int(input())
lsts = [[num]*5 for _ in range(5)]


for i in range(len(lsts)):
    if 1 <= i <= 3:
        for j in range(len(lsts[i])):
            if 1 <= j <= 3:
                lsts[i][j] = "_"

for lst in lsts:
    print(*lst,sep='')
