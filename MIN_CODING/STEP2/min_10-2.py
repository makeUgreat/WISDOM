lsts = [[0]*4 for _ in range(4)]

num = int(input())
value = 1
if num % 2 == 0:
    for i in range(len(lsts)):
        for j in range(len(lsts[i])):
            if i == j:
                lsts[i][j] = value
                value += 1

elif num % 2 == 1:
    for i in range(4):
        lsts[i][4 - i - 1] = i + 1

for lst in lsts:
    print(*lst)