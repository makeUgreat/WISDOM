import sys,heapq
sys.stdin = open('input.txt','r')

N,M = map(int,input().split())
start = int(input())
graph = [ [] for _ in range(N+1) ]
INF = int(21e8)
distance = [INF] * (N+1)

for _ in range(M):
    v,w,c = map(int,input().split())
    graph[v].append([w,c])


def dijk(start):
    st_heap = []
    heapq.heappush(st_heap, (0,start)) # 비용, 노드번호 순
    distance[start] = 0

    while st_heap:
        dist,now = heapq.heappop(st_heap)

        if distance[now] < dist: continue

        for node in graph[now]:
            adjNode = node[0]
            adjCost = node[1]

            cost = dist + adjCost  # 가려는 노드의 비용
            if cost < distance[adjNode]: # 그 비용이 저장되어잇는 정보보다 작으면
                distance[adjNode] = cost
                heapq.heappush(st_heap,(cost,adjNode))


dijk(start)

for i in range(1,len(distance)):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

