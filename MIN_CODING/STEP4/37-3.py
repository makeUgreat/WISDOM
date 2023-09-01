
import sys
sys.stdin=open('input.txt','r')
from collections import deque

def bfs():
    q = deque()

    for i in range(4):
        for j in range(5):
            if arr[i][j] == 1:
                q.append([i,j,1])

    while q:
        y,x,time = q.popleft()
        diy = [-1,1,0,0,-1,1,1,-1]
        dix = [0,0,-1,1,1,-1,1,-1]

        for i in range(8):
            dy = y + diy[i]
            dx = x + dix[i]

            if dy<0 or dx<0 or dy>=4 or dx>=5: continue
            if arr[dy][dx] != 0: continue

            arr[dy][dx] = time
            q.append([dy,dx,time+1])

    return time

arr =  []
for _ in range(4):
    row = list(map(int,input().split()))
    arr.append(row)

print(bfs()-1)
for a in arr:
    print(*a)
