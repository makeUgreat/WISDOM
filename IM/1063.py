import sys
sys.stdin = open('IM/input.txt','r')

def move(get_order):
    direction = {
        'B': (1,0),
        'T': (-1,0),
        'L': (0,-1),
        'R': (0,1),
        'RT': (-1,1),
        'LT': (-1,-1),
        'RB': (1,1),
        'LB': (1,-1)
    }
    
    return direction[get_order]
    

Map = [[1]*10] + [ [1]+[0]*8 +[1] for _ in range(8) ] + [[1]*10]
col = ['','A','B','C','D','E','F','G','H','']
row = [0,8,7,6,5,4,3,2,1,0]


king, stone, N = input().split()
N = int(N)
# 초기 좌표 저장
kx = col.index(king[0])
ky = row.index(int(king[1]))

sx = col.index(stone[0])
sy = row.index(int(stone[1]))

Map[ky][kx] = 'K'
Map[sy][sx] = 'S'

# for m in Map:
#     print(*m)
    

for g in range(N):
    order = input() 
    y,x = move(order) # 이동좌표 불러옴
    # print(f'{g+1}번째')     
    # print(y,x)
    

    
    if sy == (ky+y) and sx == (kx+x): # 이동할 곳에 돌이 있으면
        if Map[sy+y][sx+x] == 1: # 돌이 이동할 곳에 벽 있으면 패스
            continue
        sy += y
        sx += x 
        Map[sy][sx] = 'S'
        
        
    if Map[ky+y][kx+x] == 1: continue # 이동한 곳이 벽이면 패스
    Map[ky][kx] = 0
    ky += y
    kx += x 
    Map[ky][kx] = 'K'


for i in range(10):
    for j in range(10):
        if Map[i][j] =='K':
            ki = i
            kj = j
        if Map[i][j] == 'S':
            si = i
            sj = j

# for m in Map:
#     print(*m)
print(f'{col[kj]}{row[ki]}')            
print(f'{col[sj]}{row[si]}') 

    
    
