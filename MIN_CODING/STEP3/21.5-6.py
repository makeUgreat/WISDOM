maps = [
    [0,0,0,0,0,0,0],
    [0,0,1,0,1,0,0],
    [0,1,2,0,2,1,0],
    [0,0,1,2,1,0,0],
    [0,0,2,1,0,1,0],
    [0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0]
]


y,x = map(int,input().split())
maps[y][x] = 1

directy = [-1,1,0,0]
directx = [0,0,-1,1]

answer = 0    
for i in range(4):
    cnt = 0
    
    dy = y + directy[i]
    dx = x + directx[i] 
    if dy<0 or dx<0 or dy>6 or dx>6:
        continue
    if maps[dy][dx] == 2: # 착수한 자리 상하좌우에 흑돌이 있으면
        # 흑돌 좌표저장
        by = dy
        bx = dx    

        for j in range(4):  # 흑돌 상하좌우에 백돌 있으면 카운트
            bdy = by + directy[j]
            bdx = bx + directy[j]
            if bdy<0 or bdx<0 or bdy>6 or bdx>6:
                continue
            
            if maps[bdy][bdx] == 1: 
                cnt += 1 
            
        if cnt == 4: # 상하좌우 4개있으면 잡아먹고
            answer += 1  # 잡아먹은 횟수 1 카운트
        
        
print(answer)
        