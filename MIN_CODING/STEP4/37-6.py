from collections import deque
import sys
sys.stdin = open('input.txt')


arr = [list(map(int,input().split())) for _ in range(4)]
visit = [[0]*6 for _ in range(4)]
cnt = 0
def bfs(y,x):
    global cnt
    q = deque()
    q.append([y,x])

    diy = [-1,1,0,0]
    dix = [0,0,-1,1]
    while q:
        y,x = q.popleft()

        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]

            if dx<0 or dy<0 or dx>=6 or dy>=4: continue
            if arr[dy][dx] == 1: continue
            if visit[dy][dx]: continue
            visit[dy][dx] = 1

            q.append([dy,dx])
            if arr[dy][dx] == 2:
                cnt += 1


bfs(0,0)
print(cnt)
# for a in arr:
#     print(*a)