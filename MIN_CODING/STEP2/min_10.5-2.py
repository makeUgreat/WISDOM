num = int(input())
lsts = []

for i in range(5):

    if i == num:
        line = [ num for _ in range(5) ]
        lsts.append(line)
        continue

    line = [ (21 + i) - (5 * j) for j in range(5)]
    lsts.append(line)


for lst in lsts:
    print(*lst)