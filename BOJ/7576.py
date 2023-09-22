import sys
sys.stdin = open('input.txt','r')

from collections import deque

m,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]


def bfs():
    global is_flag
    q = deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                is_flag = 1
                q.append([i,j,1])

    if not is_flag: # 상자에 익은 토마토가 단 하나도 없다면
        return -1

    while q:
        y,x,days = q.popleft()

        diy = [-1,1,0,0]
        dix = [ 0,0,-1,1]
        for i in range(4):
            dy = y+diy[i]
            dx = x+dix[i]
            if dy<0 or dx<0 or dy>=n or dx>=m: continue
            if arr[dy][dx] != 0: continue

            arr[dy][dx] = days
            q.append([dy,dx,days+1])

    return days-1


is_flag = 0
flag = 0
res = bfs()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            flag = 1

if flag: print(-1)
else: print(res)
#
# for a in arr:
#     print(*a)
