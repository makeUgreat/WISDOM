import heapq,sys
sys.stdin = open('input.txt','r')

INF = int(21e8)

v,e = map(int,input().split())
start = int(input())
graph = [ [] for _ in range(v+1) ]
distance = [INF] * ( v + 1 )

# 간선 정보 받기
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    st_heap = []
    heapq.heappush(st_heap, (0,start))
    distance[start] = 0

    while st_heap:
        dist,now = heapq.heappop(st_heap)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(st_heap, (cost,i[0]))

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

