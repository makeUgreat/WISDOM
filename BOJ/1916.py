import sys,heapq
sys.stdin = open('input.txt','r')

N = int(input())
M = int(input())

graph = [ [] for _ in range(N+1) ]
INF = int(1e9)
distance = [INF] * (N+1)

for _ in range(M):
    v,w,c = map(int,input().split())
    graph[v].append([w,c])  # v도시부터 w도시까지 버스비용 c

start,destination = map(int,input().split())

def dijk(start):
    st_heap = []
    heapq.heappush(st_heap, (0,start))  #출발지 넣어주기 출발지->출발지 비용은 0
    distance[start] = 0

    while st_heap:
        dist,now = heapq.heappop(st_heap)

        if distance[now] < dist: continue

        for node in graph[now]: # 인접 노드 정보 불러오기
            adjNode = node[0]
            edgeCost = node[1]

            cost = dist + edgeCost

            # 현재까지의 비용(거리)와 앞으로의 인접 노드까지 가는데 드는 비용의 합이
            # 기존에 저장한 비용정보(가려는 노드의)보다 작으면 갱신
            if cost < distance[adjNode]:
                distance[adjNode] = cost
                # 그리고 우선순위 큐에 추가
                heapq.heappush(st_heap, (cost,adjNode))


dijk(start)

for i in range(1,N+1):
    if i == destination:
        print(distance[i])