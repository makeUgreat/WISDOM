from collections import deque

import sys
sys.stdin = open('input.txt','r')

N = int(input())
arr = list(map(int,input().split()))
visit = [False]*N

max_v =
def bfs():
    q = deque()

    for i in range(N):
        q.append([i,arr[i]])

    while q:
        idx,Sum = q.popleft()
        dix = [-1,1]

        for i in range(2):
            dx = idx + dix[i]

            if dx<0 or dx>=N: continue
            if visit[dx]: continue
            visit[dx] = True

            q.append(dx,Sum+arr[dx])


bfs()