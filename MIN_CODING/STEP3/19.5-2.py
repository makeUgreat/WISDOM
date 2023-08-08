import sys
sys.stdin = open('MIN_CODING/STEP3/input.txt','r')

# 상하좌우,대각선에 1이 없으면 안정된 상태출력


# 델타배열로 상하좌우 탐색하기

def searchAround(y,x):
    global flag
    direction = [(-1,-1),(-1,0),(-1,-1),
                 (0,-1),(0,1),
                 (1,-1),(1,0),(1,1)] # 가운데를 제외한 9방향 

    for dty,dtx in direction: 
        dy = y + dty
        dx = x + dtx 
        if dy<0 or dx<0 or dy>4 or dx>3: continue
        if arr[dy][dx] == 1: # 주변에 숫자가 있으면
            flag = 1           
        
flag = 0
arr = []
for _ in range(5):
    line = list(map(int,input().split()))
    arr.append(line)


for i in range(5):
    for j in range(4):
        if arr[i][j] == 1: 
            searchAround(i,j)
            break

if flag:
    print('불안정한 상태')
else: print('안정된 상태')
    
