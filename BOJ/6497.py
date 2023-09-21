import sys,heapq
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def findR(get_node):
    global parent
    if parent[get_node] == -1:
        return get_node
    else:
        res = findR(parent[get_node])
        parent[get_node] = res
        return res


def min_union(cost,a,b):
    global min_total,parent
    root_a = findR(a)
    root_b = findR(b)

    if root_a == root_b:
        return
    else:
        parent[root_b] = root_a
        min_total += cost

while 1:
    parent = [-1] * 200001
    min_graph = []
    min_total = 0
    Sum = 0

    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break

    for _ in range(m):
        v,w,c = map(int,input().split())
        heapq.heappush(min_graph,(c,v,w))
        Sum += c

    while min_graph:
        cost,s,e = heapq.heappop(min_graph)
        min_union(cost,s,e)

    print(Sum-min_total)
