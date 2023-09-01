from collections import deque

import sys
sys.stdin = open('input.txt','r')

N = int(input())
arr = [[0]*N for _ in range(N)]
x,y,p,q = map(int,input().split())

def bfs():
    q =deque()
    q.append([x,y,1])
    q.append([p,q,1])

    while q:
        x,y,days =`\

bfs()
