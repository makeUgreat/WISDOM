from collections import deque
import sys
sys.stdin = open('input.txt','r')

def bfs(fy,fx):
    q = deque()
    q.append([fy,fx,1])

    while q:
        y,x,time = q.popleft()

        diy = [-1,1,0,0]
        dix = [0,0,-1,1]
        for i in range(4):
            dy = y +diy[i]
            dx = x+ dix[i]

            if dy<0 or dx<0 or dy>=N or dx>=M: continue
            if arr[dy][dx] != 0: continue

            arr[dy][dx] = time
            q.append([dy,dx,time+1])

    return time


N,M = map(int,input().split())

arr = []
for _ in range(N):
    row = list(map(int,input().split()))
    arr.append(row)

fy,fx = map(int,input().split())


print(bfs(fy,fx)-1)
# for a in arr:
#     print(*a)