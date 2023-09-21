import sys,heapq
sys.stdin = open('input.txt','r')

N,M = map(int,input().split())
C,V = map(int,input().split())
parent = [-1] * (1001)

def findR(get_node):
    if parent[get_node] == -1:
        return get_node
    else:
        res = findR(parent[get_node])
        parent[get_node] = res
        return res

def union(a,b):
    root_a = findR(a)
    root_b = findR(b)

    if root_a == root_b:
        return

    else:
        parent[root_b] = root_a

# 그래프 맥스힙으로 자기
graph = []
for _ in range(M):
    v,w,c = map(int,input().split())
    heapq.heappush(graph,(-c,v,w))

answer = 0

while graph:
    wid,s,e = heapq.heappop(graph)
    wid = -wid
    union(s,e)

    if findR(C) == findR(V):
        answer = wid
        break


print(answer)
