num = int(input())

lsts = [[0]*4 for _ in range(3)]
count = num

for i in range(len(lsts)):
    for j in range(len(lsts[i])):
        if i + j >= 2:
            lsts[i][j] = count
            count += 1


# 출력

for lst in lsts:
    for ls in lst:
        if ls == 0:
            print(' ', end='')
            continue
        print(ls,end='')
    print()

