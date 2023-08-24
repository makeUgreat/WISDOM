# import sys
# sys.stdin = open('IM/input.txt','r')

C,R = map(int, input().split()) # 가로 세로
K = int(input())

arr = [[1]*(C+2)] + [[1]+[0]*C+[1] for _ in range(R)] + [[1]*(C+2)] 
# 인덱스를 위해 한 줄씩 추가

if R*C < K:
    print(0)
else:
    
    diry = [1,0,-1,0]
    dirx = [0,1,0,-1]
    
    ci,cj = 1,1
    dr = 0
    ni,nj = 0,0
    
    for n in range(1,K):
        arr[ci][cj] = n
        ni = ci + diry[dr]
        nj = cj + dirx[dr]
        
        if arr[ni][nj] == 0:
            ci,cj = ni,nj 
        else: 
            dr = (dr+1)%4 
            ci = ci + diry[dr]
            cj = cj + dirx[dr]

    print(f'{cj} {ci}')
