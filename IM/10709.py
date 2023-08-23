import sys
sys.stdin = open('IM/input.txt','r')


H,W = map(int, input().split()) # 세로 , 가로

Map = []
for _ in range(H):
    row = list(input())
    Map.append(row)
    
for i in range(H):
    cidx = 0
    num = 0
    for j in range(W):
        if Map[i][j] == '.':
            Map[i][j] = -1
            
        if Map[i][j] == 'c':
            num = 0
            cidx = j 
            Map[i][j] = num
            
            for k in range(j+1, W):
                if Map[i][k] == 'c':
                    break
                num += 1
                Map[i][k] = num
        
for m in Map:
    print(*m)