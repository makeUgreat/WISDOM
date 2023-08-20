from collections import deque
n = int(input())

Map = []
for _ in range(n):
    row = list(map(int,input().split()))
    Map.append(row)
visit = [[0] * n for _ in range(n)]

flag = 0
def bfs(y,x):
    global flag
    q = deque([[y,x]])
    visit[y][x] = 1
    
    while q: 
                
        yy,xx = q.popleft()
        diry = [-1,1,0,0]
        dirx = [0,0,-1,1]
        
        for i in range(4):
            dy = yy + diry[i]
            dx = xx + dirx[i]
            
            if dy<0 or dx<0 or dy>=n or dx>=n: continue
            if visit[dy][dx] == 1: continue
            if Map[dy][dx] == 1: continue 
        
            visit[dy][dx] = 1
            q.append([dy,dx])
        
            if dy == n-1 and dx == n-1:
                flag = 1
                return
bfs(0,0)

if flag: print('가능')
else: print('불가능')

