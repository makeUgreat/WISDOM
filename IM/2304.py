import sys
sys.stdin = open('input.txt','r')

N = int(input())

# 가장 큰 값으로 맵 제작하기
Map = [['.'] * 20 for _ in range(20)]
max_L = 0
max_H = 0
min_L = 0
min_H =0
for _ in range(N):
    L,H = map(int, input().split())

    for i in range(H):
        Map[i][L] = 1

    max_L = max(max_L,L)
    max_H = max(max_H,H)
    min_L = min(min_L,L)
    min_H = min(min_H,H)

def delta(y,x):
    diry = [-1,1,0,0]
    dirx = [0,0,-1,1]

    for i in range(4):
        dy = y + diry[i]
        dx = x + dirx[i]

        if dy < 0 or dx <0 or dy>1000 or dx >1000: continue
        if Map[dy][dx] != '.': continue

        Map[dy][dx] = 0



print(max_H)

for i in range(max_H+1):
    for j in range(max_L+1):
        if Map[i][j] == 1:
            delta(i,j)

for m in Map:
    print(*m)
