# A 아스키코드 65
# M 아스키코드 77

lsts = []
for i in range(5,-1,-1):
    line = []
    for j in range(77+i,64+i,-6):  #A부터 M까지 열 갯수 6만큼
        line.append(chr(j))
    lsts.append(line)

y,x  = map(int,input().split())

print(lsts[y][x])