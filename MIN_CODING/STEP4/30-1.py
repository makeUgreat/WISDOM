adj_matrix = [
    [0,0,1,1,0,1],
    [0,0,0,1,1,1],
    [0,0,0,0,1,1],
    [0,0,0,0,0,0],
    [1,0,0,0,0,1],
    [0,0,0,0,0,0]    
]
name = [0,1,2,3,4,5]
visit = [False]*6
start = int(input())
def dfs(now):
    
    visit[now] = True
    print(name[now],end=' ')
    

    for i in range(6):
        if adj_matrix[now][i] == 1 and not visit[i]:
            dfs(i)
        
    

dfs(start)

