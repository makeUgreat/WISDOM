N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
path = [0] * M 
min_path = [0] * M
visit = [False] * N
min_v = 21e8

def abc(level,mul):
    global min_v,min_path
    
    if level == M:
        if mul < min_v:
            min_v = mul 
            min_path = path.copy() 
        return
        
        
        
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            path[level] = nums[i]
            abc(level+1, mul*nums[i]) 
            visit[i] = 0
    
abc(0,1)
print(*min_path)