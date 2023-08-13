def dfs(node, matrix, path, level):
    if level == 2:
        for i in range(3):
            print(path[i],end=' ')
        print()
    
    for i in range(len(matrix)):
        if matrix[node][i] == 1:
            path.append(i)
            dfs(i,matrix,path, level+1)
            path.pop() 
    
     

node = int(input())
path = []
matrix = []

for _ in range(node):
    line = list(map(int,input().split()))
    matrix.append(line)
    
for i in range(node):
    dfs(i, matrix, [i], 0)