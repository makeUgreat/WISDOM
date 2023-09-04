from collections import deque
import sys
sys.stdin = open('input.txt','r')

def delta(y,x,check):
    q = deque()
    q.append([y,x])

    visit[y][x] = True

    while q:
        y,x = q.popleft()
        arr[y][x] = 0

        diy = [-1,1,0,0]
        dix = [0,0,-1,1]
        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]
            if dy<0 or dx<0 or dy>=8 or dx>=9: continue
            if arr[dy][dx] != '#':continue
            if visit[dy][dx]: continue
            visit[dy][dx]=True
            if check == 1: man1.append((dy,dx))
            if check == 2: man2.append((dy,dx))
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

for a in arr:
    print(*a)

print(man1)
print(man2)