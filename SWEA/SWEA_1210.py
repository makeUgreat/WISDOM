import sys
sys.stdin = open('SWEA/input.txt','r')

from collections import deque

for tc in range(1,11):
    
    t = int(input())
    
    Map = []
    for _ in range(100):
        row = list(map(int,input().split()))
        Map.append(row)
        
    for i in range(100):
        if Map[99][i] == 2:
            start_index = i 
            

    q = deque([[99,start_index]])    

    ans = 0
    while q:
        
        y,x = q.popleft()
        
        diry = [0,0,-1]
        dirx = [-1,1,0]
        
        for i in range(3):
            dy = y + diry[i]
            dx = x + dirx[i] 
            
            if dy<0 or dx<0 or dy>99 or dx>99: continue
            if Map[dy][dx] == 0: continue
            
            Map[y][x] = 0 
            if dy == 0:
                ans = dx 
                
            q.append([dy,dx])
            
            
            if Map[dy][dx] == 1:
                break   
        
    print(f'#{tc} {ans}')