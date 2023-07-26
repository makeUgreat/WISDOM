n1, n2 = map(int,input().split())
lsts = []

for i in range(6):
    line = [ (10 + i) + (6 * j)  for j in range(3)]
    lsts.append(line)

for k in range(n1,n2+1):
    for j in range( len( lsts[i] ) ):
            lsts[k][j] = 7





for lst in lsts:
    print(*lst)