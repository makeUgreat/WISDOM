import sys,heapq
sys.stdin = open('input.txt','r')

N,M = map(int,input().split())
#초기화
graph = [ [] for _ in range(N+1) ]
INF = int(21e8)
distance = [INF] * (N+1)

# 그래프 정보 받기
for _ in range(M):
    v,w,c = map(int,input().split())
    graph[v].append([w,c])

def dijk(start):
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


dijk(0) # strat -> 0, end -> N-1


for i in range(N):
    if i == N-1:
        if distance[i] == INF:
            print('impossible')
        else:
            print(distance[i])

