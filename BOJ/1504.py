import sys,heapq
sys.stdin = open('input.txt','r')
input = sys.stdin.readline


n,m = map(int,input().split())
graph = [ [] for _ in range(n+1) ]
INF = int(21e8)

for _ in range(m):
    v,w,c = map(int,input().split())
    graph[v].append([w,c])
    graph[w].append([v,c])

v1,v2 = map(int,input().split())

def dijk(start):
    distance = [INF] * (n+1)
    st_heap = []
    heapq.heappush(st_heap,(0,start))
    distance[start] = 0

    while st_heap:
        dist,now = heapq.heappop(st_heap)

        if distance[now] < dist: continue

        for node in graph[now]:
            adjNode = node[0]
            adjCost = node[1]

            cost = dist + adjCost

            if cost < distance[adjNode]:
                distance[adjNode] = cost
                heapq.heappush(st_heap,(cost,adjNode))

    return distance


st_dist = dijk(1)
v1_dist = dijk(v1)
v2_dist = dijk(v2)

res = min(
    st_dist[v1] + v1_dist[v2] + v2_dist[n],
    st_dist[v2] + v2_dist[v1] + v1_dist[n]
)

if res >= INF: print(-1)
else: print(res)
