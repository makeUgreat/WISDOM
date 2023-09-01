from collections import deque

import sys
sys.stdin = open('input.txt','r')

def bfs(x,y,t,v):
    q = deque()
    q.append([x,y,2])
    q.append([t,v,2])

    while q:
        x,y,days = q.popleft()

        diy = [-1,1,0,0]
        dix = [0,0,-1,1]

        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]

            if dy<0 or dx<0 or dx>=N or dy>=N: continue
            if arr[dy][dx] != 0: continue

            arr[dy][dx] = days
            q.append([dy,dx,days+1])

N = int(input())
arr = [[0]*N for _ in range(N)]
x,y,t,v = map(int,input().split())
arr[x][y] = 1
arr[t][v] = 1

bfs(x,y,t,v)

for a in arr:
    print(*a,sep='')