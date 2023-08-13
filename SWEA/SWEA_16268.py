import sys
sys.stdin = open("SWEA/input.txt","r")

T = int(input())

for tc in range(1,T+1):
    
    n,m = map(int,input().split())
    lsts = []
    for _ in range(n):
        line = list(map(int,input().split()))
        lsts.append(line)
        
    
    def getSum(y,x):
        Sum = 0    
        direction = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]
        for yy,xx in direction:
            if y+yy >= 0 and x+xx >= 0 and y+yy < n and x+xx < m:
                Sum += lsts[y+yy][x+xx]
        
        return Sum
    
    max_v = -21e8
    for i in range(n):
        for j in range(m):
            if getSum(i,j) > max_v:
                max_v = getSum(i,j)
                
    print(f'#{tc} {max_v}')