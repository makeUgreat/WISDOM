from collections import deque
import sys
sys.stdin = open('input.txt','r')

arr = [
    [0,0,0,0],
    [1,1,0,1],
    [0,0,0,0],
    [1,0,1,0]
]

def bfs(sy,sx,ey,ex):
    q = deque()
    q.append([sy,sx,1])

    while q:
        y,x,step = q.popleft()
        diy = [-1,1,0,0]
        dix = [0,0,-1,1]

        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]

            if dy<0 or dx<0 or dy>=4 or dx>=4: continue
            if arr[dy][dx] != 0: continue
            arr[dy][dx] = step
            q.append([dy,dx,step+1])

            if dy == ey and dx == ex:
                return step



sy,sx = map(int,input().split())
ey,ex = map(int,input().split())

print(f'{bfs(sy,sx,ey,ex)}회')

# for a in arr:
#     print(*a)