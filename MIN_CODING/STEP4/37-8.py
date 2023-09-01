from collections import deque
import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]


def bfs(y,x):
    q = deque()
    q.append([y,x])

    while q:
        y,x = q.popleft()

        diy = [-1,1,0,0]
        dix = [0,0,-1,1]
        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]

            if dy<0 or dx<0 or dy>=N or dx>=M: continue
            if arr[dy][dx] != 1: continue

            arr[dy][dx] = 0
            q.append([dy,dx])

    return 1

Sum = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            Sum += bfs(i,j)

            # for a in arr:
            #     print(*a)
            # print()

print(Sum)
