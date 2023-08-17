from collections import deque

adj_matrix = [
    [0,1,0,0,1,0],
    [0,0,1,0,0,1],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

start = int(input())
name = [0,1,2,3,4,5]
visit = [False] * 6


q = deque()
q.append(start) 
visit[start] = True
    
while q:
    v = q.popleft()
    print(name[v],end=' ')
    
    for i in range(6):
        if adj_matrix[v][i] == 1 and not visit[i]:
            q.append(i) 

