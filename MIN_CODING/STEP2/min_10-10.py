num = int(input())
lsts = []

for i in range(3):
    line = [12 - (4 * i) - j for j in range(4)]
    lsts.append(line)

for i in range(len(lsts)):
    for j in range(len(lsts[i])):
        if j == num:
            lsts[i][j] = 0
    


for lst in lsts:
    print(*lst)