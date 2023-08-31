def findP(get_node):
    if parent[get_node] == 0:
        return get_node

    else:
        res = findP(parent[get_node])
        return res

def union(a,b):
    global cnt
    root_a = findP(a)
    root_b = findP(b)

    if root_a == root_b:
        return
    else:
        parent[root_b] = root_a
        cnt -= 1

cnt = 10
parent = [0] * 200
union(ord('A'),ord('B'))
union(ord('A'),ord('C'))
union(ord('E'),ord('D'))
union(ord('E'),ord('F'))
union(ord('H'),ord('G'))
union(ord('I'),ord('J'))

N = int(input())

for _ in range(N):
    a,b = map(ord,input().split())
    union(a,b)

print(f'{cnt}개')