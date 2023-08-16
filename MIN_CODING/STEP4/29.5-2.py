timeStamp = [8,3,5,6,8,9,10] 


adj_list = [
    [-1],
    [0],
    [0],
    [1],
    [2],
    [4],
    [4],
]

visited = [False]*7
start = int(input())

def dfs(node):
    visited[node] = True

    if node == -1:
        return
    
    for i in adj_list[node]:
        if not visited[i]:
            dfs(i)
            if node == 0:
                print(f'{node}번index(출발)',end=' ')
                print()
            
            else:
                print(f'{node}번index({timeStamp[node]}시)',end=' ')
                print()

dfs(start)