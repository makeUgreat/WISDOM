import sys
sys.stdin = open('input.txt','r')
from collections import deque

n,m = map(int,input().split())
sy,sx,head = map(int,input().split())
arr = [ list(map(int,input().split())) for _ in range(n)]


cnt = 0
def bfs(sy,sx,head):
    global cnt
    q = deque()
    q.append([sy,sx,head])
    arr[sy][sx] = 2  # 청소표시
    cnt += 1

    while q:
        y,x,head = q.popleft()
        flag = 1
        # 주변 4칸 중 청소되지 않은 빈칸이 있는 경우

        for _ in range(4):
            head = (head - 1) % 4
            ny = [0, -1, 0, 1][head]
            nx = [-1, 0, 1, 0][head]

            dy = y + ny
            dx = x + nx

            if dy<0 or dx<0 or dy>=n or dx>=m: continue

            # 바라보는 방향이 청소되지 않은 빈칸을 향할 때까지
            # 반시계 방향으로 90도 회전
            if arr[dy][dx] == 0:
                flag = 0
                dy2 = 0
                dx2 = 0
                while 1:
                    if dy2 == dy and dx2 == dx:
                        # 청소되지 않은 방향을 바라보면 전진
                        q.append([dy,dx,head%4])
                        break

                    head += 1  # 반시계 방향으로 90도 회전
                    dy2 = dy + diy[head%4]
                    dx2 = dx + dix[head%4]

        if flag: # 주변 4칸에 청소할 칸이 없으면
            # 바라보는 방향 유지하고 한 칸 후진
            dy = y+diy[(head+2)%4]
            dx = x+dix[(head+2)%4]
            if arr[dy][dx] == 1:
                break
            q.append([dy,dx,head%4])




bfs(sy,sx,head)
print(cnt)