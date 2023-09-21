import sys
sys.stdin = open('input.txt','r')

N,M = map(int,input().split())
visit = [[False]*M for _ in range(N)]
y,x,head = map(int,input().split())
visit[y][x] = 1
Map = [list(map(int,input().split())) for _ in range(N)]

diy = [-1,0,1,0]
dix = [0,1,0,-1]

def turn_left():
    global head
    head -= 1
    if head == -1:
        head = 3

cnt = 1
turn_time = 0

while True:
    turn_left()
    ny = y + diy[head]
    nx = x + dix[head]

    if Map[ny][nx] == 0 and not visit[ny][nx]:
        visit[ny][nx] = 1
        y = ny
        x = nx
        cnt += 1
        turn_time = 0
        continue

    # 가봤거나 바다면
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없으면

    if turn_time == 4:
        ny = y - diy[head]
        nx = x - dix[head]

        if Map[ny][nx] == 0:
            y = ny
            x = nx
        else:
            break

        turn_time = 0

print(cnt)
