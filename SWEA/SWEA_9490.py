import sys
sys.stdin = open('WISDOM/SWEA/input.txt','r')

def deltaSum(y,x,get_arr,value):
    Sum = 0
    
    diry = [0,-1,1,0,0]
    dirx = [0,0,0,-1,1]
    for j in range(1,value+1):
        for i in range(5):
            dy = y + (diry[i] * j)
            dx = x + (dirx[i] * j)
        
            if dy<0 or dx<0 or dy>= n or dx>= m: continue
            Sum += get_arr[dy][dx] 
        
    return Sum
        
        

    

T = int(input())
for tc in range(1,T+1):
    
    n,m = map(int,input().split())
    
    #배열 생성
    arrs = []
    for _ in range(n):
        row = list(map(int,input().split()))
        arrs.append(row)
        
    max_v = -21e8
    #배열 순회하면서 합
    for i in range(n):
        for j in range(m):
            if deltaSum(i,j,arrs,arrs[i][j]) > max_v:
                max_v = deltaSum(i,j,arrs,arrs[i][j])

    
    
    print(f'#{tc} {max_v}')