adj_matrix = [
    [0,0,1,0,2,0],
    [5,0,3,0,0,0],
    [0,0,0,0,0,7],
    [2,0,0,0,8,0],
    [0,0,9,0,0,0],
    [4,0,0,7,0,0],
]
name = [0,1,2,3,4,5] 
# def dfs(now,cost):
#     global Sum
#     visit[now] = True
#     print(name[now],cost)

    
#     for i in range(6):
#         if adj_matrix[now][i] >= 1 and not visit[i]:
#             dfs(i, cost + adj_matrix[now][i])

# start = int(input())
# visit = [False] * 6
# dfs(start,0)

Sum = 0
def dfs(now):
    global Sum
    visit[now] = True
    print(name[now], Sum)

    
    for i in range(6):
        if adj_matrix[now][i] >= 1 and not visit[i]:
            Sum += adj_matrix[now][i]
            dfs(i)

start = int(input())
visit = [False] * 6
dfs(start)