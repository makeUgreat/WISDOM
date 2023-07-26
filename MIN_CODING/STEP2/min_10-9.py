tmp = []

for i in range(4):
    line = [ 13 + i - (4 * j) for j in range(4)]
    tmp.append(line)


for i in tmp:
    print(*i)