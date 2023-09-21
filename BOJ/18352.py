import sys,heapq
sys.stdin = open('input.txt','r')

'''
1. 출발 노드의 간선비용 모두 저장

'''

N,M,K,X = map(int,input().split()) #정점,간선,거리,출발노드
# 초기화
graph = [ [] for _ in range(N+1) ]
INF = int(21e8)
distance = [INF] * (N+1)

# 간선 정보 입력
for _ in range(M):
    v,w = map(int,input().split()) # v노드에서 w노드까지 1의 거리
    graph[v].append((w,1))

def dijk(start):
    st_heap = []
    heapq.heappush(st_heap, (0,start))  # 비용(거리),노드순으로 저장(비용순으로 정렬하기위해)
    distance[start] = 0

    while st_heap:
        dist,now = heapq.heappop(st_heap) # 거리, 현재노드위치

        # 현재 노드가 처리된 적 있던 노드면 무시
        if distance[now] < dist:
            continue

        for node in graph[now]: #현재 노드와 인접한 노드들 확인
            adj_node = node[0]
            edge_cost = node[1]

            cost = dist + edge_cost # 현재 노드 비용 + 인접 노드 비용

            if cost < distance[adj_node]:
                distance[adj_node] = cost
                heapq.heappush(st_heap, (cost, adj_node))


dijk(X)

flag = 1
for i in range(N+1):
    if distance[i] == K:
        print(i)
        flag = 0

if flag: print(-1)