def findP(get_node):
    # 입력받은 노드의 부모정보가 없으면 본인이 루트노드
    if parent[get_node] == 0:
        return get_node

    else: # 부모 정보가 있으면

        res = findP(parent[get_node]) # 부모의 부모... 까지 재귀탐색
        return res

def union (a,b):
    global flag
    root_a = findP(a)
    root_b = findP(b)

    if root_a == root_b: #싸이클이면
        flag = 1
        return

    parent[root_b] = root_a


N = int(input())
flag = 0
parent = [0] * (200)

for _ in range(N):
    a,b = map(ord,input().split())
    union(a,b)


if flag: print('발견')
else: print('미발견')