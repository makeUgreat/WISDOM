import sys
sys.stdin = open('input.txt','r')

from collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]


# 레드 0 그린 1 블루 2
rgb = ['R','G','B']
diy = [-1,1,0,0]
dix = [0,0,-1,1]


def bfs(sy,sx,color):
    q = deque()
    q.append([sy,sx])

    if color == 'B':
        arr[sy][sx] = 2
    elif color == 'R' or color == 'G':
        arr[sy][sx] = 1

    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]
            if dy<0 or dx<0 or dy>=n or dx>=n: continue
            if arr[dy][dx] != color: continue

            if arr[dy][dx] == 'B':
                arr[dy][dx] = 2
                q.append([dy,dx])
                continue

            elif arr[dy][dx] == 'R' or arr[dy][dx] =='G':
                arr[dy][dx] = 1
                q.append([dy,dx])
                continue


def bfs2(sy,sx,number):
    q = deque()
    q.append([sy,sx])
    arr[sy][sx] = 0

    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]
            if dy<0 or dx<0 or dy>=n or dx>=n: continue
            if arr[dy][dx] != number: continue

            arr[dy][dx] = 0
            q.append([dy,dx])

cnt_max,cnt_min = 0,0

# 일반인 구역
for i in range(n):
    for j in range(n):
        if arr[i][j] in rgb:
            cnt_max += 1
            bfs(i,j,arr[i][j])

# 적록색약 구역
for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            cnt_min += 1
            bfs2(i,j,arr[i][j])

print(cnt_max)
print(cnt_min)