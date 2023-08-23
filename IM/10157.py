# import sys
# sys.stdin = open('IM/input.txt','r')
from collections import deque

C,R = map(int, input().split()) # 가로 세로

Map = [ [0] * C for _ in range(R) ]  # 인덱스를 위해 한 줄씩 추가
diry = [-1,0,1,0]
dirx = [0,1,0,-1]


num = 1
y,x = 0,0
while 1:  

    if num >= C*R:
        break

    for i in range(4):
        for j in range(1, max(C,R)):
            dy = y + (diry[i]*j)
            dx = x + (dirx[i]*j)
        

            if dy < 0 or dx < 0 or dy > R-1 or dx > C-1: continue
            if Map[dy][dx] != 0: continue            
            Map[dy][dx] = num
            num += 1
            
        y = dy
        x = dx

            
                    


for m in Map:
    print(*m)