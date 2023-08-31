def findP(get_node):
    if parent[get_node] == -1:
        return get_node

    else:
        res = findP(parent[get_node])
        return res

def union(a,b):
    global flag
    root_a = findP(a)
    root_b = findP(b)

    if root_a == root_b:
        flag = 1
        return
    else:
        parent[root_b] = root_a


N = int(input())
adj = [list(map(int,input().split())) for _ in range(N)]

flag = 0
parent = [-1] * (N+1)
for i in range(N):
    for j in range(i,N):
        if adj[i][j] == 1:
            union(i,j)

if flag: print('cycle 발견')
else: print('미발견')