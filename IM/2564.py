import sys
sys.stdin = open('input.txt','r')

from collections import deque

m,n = map(int,input().split())
markets = int(input())

Map = [ [-1]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i == 0 or i == n or j == 0 or j == m:
            Map[i][j] = 0


for market_num in range(1, markets+2):
    data = list(map(int,input().split()))

    if data[0] == 1:  # 북쪽이면
        Map[0][data[1]] = market_num

    if data[0] == 2: # 남쪽이면
        Map[n][data[1]] = market_num

    if data[0] == 3: # 서쪽이면
        Map[data[1]][0] = market_num

    if data[0] == 4:  # 동쪽이면
        Map[data[1]][m] = market_num

for M in Map:
    print(*M)
# 시작 좌표 찾기
start_point = markets+1
for i in range(n+1):
    for j in range(m+1):
        if Map[i][j] == start_point:
            si = i
            sj = j

def searchPath(market,step):
    q = deque([[si,sj,step]])

    while q:
        y,x,step = q.popleft()
        # print(f'y={y},x={x},step={step}')
        step += 1

        diry = [-1,1,0,0]
        dirx = [0,0,-1,1]

        for i in range(4):
            dy = y + diry[i]
            dx = x + dirx[i]

            if dy<0 or dx<0 or dy >= n+1 or dx >= m+1: continue
            if Map[dy][dx] == -1: continue
            if visit_Map[dy][dx] == 1: continue

            visit_Map[dy][dx] = 1
            q.append([dy,dx,step])

            if Map[dy][dx] == market:
                return step

Sum = 0
# searchPath(1,0)
for market in range(1,markets+1):
    visit_Map = [[0]*(m+1) for _ in range(n+1)]
    Sum += searchPath(market,0)

print(Sum)


