node = int(input())
matrix = []
for _ in range(node):
    line = list(map(int,input().split()))
    matrix.append(line)

def dfs(now):
    
    print(now,end=' ')
    
    for i in range(node):
        if matrix[now][i] == 1:
            dfs(i)
    

dfs(0)