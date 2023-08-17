from collections import deque

start = int(input())

adj_matrix =[
    [0,0,0,0,1,0],
    [1,0,1,0,0,1],
    [1,0,0,1,0,0],
    [1,1,0,0,0,0],
    [0,1,0,1,0,1],
    [0,0,1,1,0,0]
]

visit = [False] * 6

q = deque()
q.append(start)
visit[start] = True

while q:
    v = q.popleft()
    print(v)

    for i in range(6):
        if adj_matrix[v][i] == 1 and not visit[i]:
            visit[i] = Tr
            q.append(i)

