from collections import deque

import sys
sys.stdin = open('input.txt','r')


arr = [list(map(int,input().split())) for _ in range(4)]

def delta(y,x,value):
    global cnt
    visit = [[False] * 9 for _ in range(4)]
    diy = [-1,1,0,0]
    dix = [0,0,-1,1]

    q = deque()
    q.append([y,x])
    visit[y][x] = True

    while q:

        y,x = q.popleft()
        # print(y,x)

        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]

            if dy<0 or dx<0 or dy>=4 or dx>=9: continue
            if visit[dy][dx]: continue
            if arr[dy][dx] == value:
                visit[dy][dx] = True
                q.append([dy,dx])
                cnt += 1

max_v = -21e8
max_i = 0
max_j = 0
for i in range(4):
    for j in range(9):
        cnt = 1
        delta(i,j,arr[i][j])
        if cnt > max_v:
            max_v = cnt
            max_i = i
            max_j = j

print(max_v*arr[max_i][max_j])
