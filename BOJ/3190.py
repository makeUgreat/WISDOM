import sys
sys.stdin = open('input.txt','r')
from collections import deque

direction = 0
def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

def bfs(sy,sx):
    q = deque()
    q.append([sy,sx])

    arr[0][0] = 1
    time = 0
    while q:
        time += 1
        y,x = q.popleft()
        print(y,x,time)


        diy = [-1,0,1,0] # 상우하좌
        dix = [0,1,0,-1]

        dy = y + diy[direction]
        dx = x + dix[direction]
        # 벽 부딪히면 끝
        if dy<0 or dx<0 or dy>=N or dx>=N:
            return time
        if arr[dy][dx] == 1:
            return time

        # 사과를 먹으면
        if arr[dy][dx] == 'A':
            arr[dy][dx] = 1
            q.append([dy,dx])
            if time in dirDict:
                turn(dirDict[time])

        elif arr[dy][dx] == 0:
            arr[dy][dx] = 1
            q.append([dy,dx])
            ty,tx = q.popleft()
            arr[ty][tx] = 0
            if time in dirDict:
                turn(dirDict[time])


# N*N 배열
N = int(input())
arr = [[0]*N for _ in range(N)]

#사과 위치정보
K = int(input())
for _ in range(K):
    y,x = map(int,input().split())
    arr[y-1][x-1] = 'A'

# 이동 명령어
L = int(input())
dirDict = dict()
for _ in range(L):
    X,C = input().split()
    dirDict[int(X)] = C

print(bfs(0,0))

