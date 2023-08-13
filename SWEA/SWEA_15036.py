import sys
sys.stdin = open("SWEA/input.txt","r")

T = int(input())

for tc in range(1,T+1):
    
    vector, edge = map(int,input().split())
    
    lsts = [[] for _ in range(vector+1)] 
    visited = [0] * (vector+1)
    
    for _ in range(edge):
        n,m = map(int,input().split())
        lsts[n].append(m)
        
    s, g = map(int,input().split())
    flag = 0
    
    def dfs(now):
        global flag
        
        for i in lsts[now]:
            
            if i == g:
                flag = 1
            
            if visited[i] == 1: continue
            visited[i] = 1
            dfs(i)
            visited[i] = 0
    
    dfs(s)
    
    print(f'#{tc} {flag}')
        