from collections import deque
import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
arr = [list(input().split()) for _ in range(N)]
visit = [[False]*M for _ in range(N)]


def bfs(yy,xx,pp,qq):
    q = deque()
    q.append([yy,xx,1])
    visit[yy][xx]= True

    while q:
        y,x,step = q.popleft()

        diy = [-1,1,0,0]
        dix = [0,0,-1,1]

        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]

            if dy<0 or dx<0 or dy>=N or dx>=M: continue
            if arr[dy][dx] == 'x': continue

            if visit[dy][dx]: continue
            # arr[dy][dx] = step
            q.append([dy,dx,step+1])
            visit[dy][dx] = True

            if dy==pp and dx==qq:
                # print(step)
                return step

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S':
            sy,sx = i,j
        if arr[i][j] == 'C':
            cy,cx = i,j
        if arr[i][j] == 'D':
            Dy,Dx = i,j

Sum = 0
Sum += bfs(sy,sx,cy,cx)
# for a in arr:
#     print(*a)
visit = [[False] * M for _ in range(N)]

Sum += bfs(cy,cx,Dy,Dx)
# for a in arr:
#     print(*a)

print(Sum)
