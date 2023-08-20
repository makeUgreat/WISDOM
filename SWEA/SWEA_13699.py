import sys
sys.stdin = open('SWEA/input.txt','r')
T = int(input())

for tc in range(1,T+1):
    
    n = int(input())
    
    area = [[0]*10 for _ in range(10)]
    
    for _ in range(n):
        sy,sx,ey,ex,color = map(int,input().split())
        
        
        for i in range(sy,ey+1):
            for j in range(sx,ex+1):
                area[i][j] += color 
                
        
    cnt = 0
    for i in range(10):
        for j in range(10):
            if area[i][j] >= 3:
                cnt += 1
    
    
    print(f'#{tc} {cnt}')
            