from collections import deque

def delta(y,x,check):
    q = deque()
    q.append([y,x])

    visit[y][x] = True

    while q:
        y,x = q.popleft()
        arr[y][x] = 0
        if check == 1: man1.append((y,x))
        if check == 2: man2.append((y,x))

        diy = [-1,1,0,0]
        dix = [0,0,-1,1]
        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]
            if dy<0 or dx<0 or dy>=8 or dx>=9: continue
            if arr[dy][dx] != '#': continue
            if visit[dy][dx]: continue
            visit[dy][dx]=True
            q.append([dy,dx])





arr = [list(input()) for _ in range(8)]
visit = [[False] * 9 for _ in range(8)]
man1 = []
man2 = []
flag = 0
for i in range(8):
    for j in range(9):
        if arr[i][j] == '#':
            delta(i,j,1)
            flag = 1
            break
    if flag: break

for i in range(8):
    for j in range(9):
        if arr[i][j] == '#':
            delta(i,j,2)
#
# for a in arr:
#     print(*a)

# abs(x1-x2) + abs(y1-y2)

min_v = 21e8
for num2 in man2:
    for num1 in man1:
        min_v = min(min_v,(abs(num2[0]-num1[0]) + abs(num2[1]-num1[1]))-1)


print(min_v)
