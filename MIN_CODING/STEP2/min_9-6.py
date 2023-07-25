num_str = ord('A')
lsts = [ [0]*3 for _ in range(3) ]
for i in range(3):
    for j in range(3):
        lsts[i][j] = chr( num_str )
        num_str += 1

y1, x1 = map(int,input().split())
y2, x2 = map(int,input().split())

tmp = lsts[y1][x1]
lsts[y1][x1] = lsts[y2][x2]
lsts[y2][x2] = tmp

for i in lsts:
    for j in i:
        print(*j,end='')
    print()