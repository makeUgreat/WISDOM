import sys
sys.stdin = open('input.txt','r')

from collections import deque


def bfs(y,x):
    cnt = 0
    q = deque()
    q.append([y,x])

    while q:
        y,x = q.popleft()

        diy = [-1,1,0,0]
        dix = [0,0,-1,1]

        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]

            if dy<0 or dx<0 or dx>=4 or dy>=4: continue
            if arr[dy][dx] == 0: continue

            arr[dy][dx] = 0
            cnt += 1
            q.append([dy,dx])
            # print(cnt)
            # for a in arr:
            #     print(*a)

    return cnt




arr = [ list(map(int,input().split())) for _ in range(4) ]


max_v = -21e8
for i in range(4):
    for j in range(4):
        if arr[i][j] == 1:
            max_v = max(max_v,bfs(i,j))

print(max_v)
