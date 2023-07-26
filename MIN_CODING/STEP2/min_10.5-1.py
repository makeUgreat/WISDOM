lsts = []
for i in range(4):
    line = [ (2 + (2*i)) + (8*j) for j in range(4)]
    lsts.append(line)

for lst in lsts:
    print(*lst)
