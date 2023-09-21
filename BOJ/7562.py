from collections import deque

import sys
sys.stdin = open('input.txt','r')


def bfs(nx,ny,ex,ey):
    q = deque()
    q.append([ny,nx,1])
    visit[ny][nx] = True

    while q:
        y,x,cnt = q.popleft()

        direction = [(-2,-1),(-2,1),
                     (-1,2),(1,2),
                     (2,-1),(2,1),
                     (-1,-2),(1,-2)]

        for yy,xx in direction:
            dy = y + yy
            dx = x + xx

            if dy<0 or dx<0 or dy>=I or dx>=I: continue
            if visit[dy][dx]: continue

            if dy==ey and dx==ex:
                return cnt

            visit[dy][dx] = True
            q.append([dy,dx,cnt + 1])

    return 0








T = int(input()) # 테케
for tc in range(T):
    I = int(input()) # 체스판 한 변의 길이
    visit = [[False] * I for _ in range(I)]
    nx,ny = map(int,input().split())
    ex,ey = map(int,input().split())

    print(bfs(nx,ny,ex,ey))


