from collections import deque
# N 입력받은 후 N x N 사이즈의 맵에 바이러스를 투입해 보자고 합니다.
# 바이러스를 최초로 투입 할 좌표를 입력 받습니다.
# 0,1 좌표에는 몇일날 바이러스가 도착 할까요?


n = int(input())

Map = [ [0]*n for _ in range(n) ]
visited = [ [0]*n for _ in range(n) ]
y,x = map(int,input().split())

q = deque() 
q.append( (y,x) )
visited[y][x] = 1

while q:
    now = q.popleft()
    y,x = now 

    directy = [-1,1,0,0]
    directx = [0,0,-1,1]

    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]

        if dy<0 or dx<0 or dy>=n or dx>=n: continue
        if visited[dy][dx] != 0: continue

        visited[dy][dx] = 1
        Map[dy][dx] = Map[y][x] + 1
        q.append( (dy,dx) )

    result = Map[0][1]+1


print(result)


