
import sys
sys.stdin = open('input.txt','r')

arr = [list(map(int,input())) for _ in range(7)]

def delta(y,x,value):
    global flag
    visit = [[False] * 7 for _ in range(7)]
    visit[y][x] = True

    diy = [-1,1,0,0]
    dix = [0,0,-1,1]

    for i in range(4):
        for step in range(1,4):
            if value == 1 and step >= 3: continue
            dy = y + diy[i]*step
            dx = x + dix[i]*step

            if dy<0 or dx<0 or dy>=7 or dx>=7: continue
            if visit[dy][dx]: continue

            visit[dy][dx] = True
            if arr[dy][dx] == value: # 만일 2,3칸 범위내에 자기와 같은 해물이 있으면
                flag = 1 # fail 플래그

flag = 0
for i in range(7):
    for j in range(7):
        if arr[i][j] > 0:
            delta(i,j,arr[i][j])

if flag: print('fail')
else: print('pass')