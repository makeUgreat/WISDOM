'''
#0 인접리스트로 단방향 그래프 만든다
#1 n명의 학생들의 출발,도착지,시간(v,w,c) 을 한명식 입력받는다
#2 v,w - > v에서 w로 가는 최소비용을 구한다
#3 w,v -> w에서 v로 가는 최소비용을 구한다
#4 둘을 더 하고 max_v 에 저장한다 max_v는 앞으로 최대값을 만나면 갱신한다
#5 모든 입력을 받을 떄까지 1~4를 반복한다
'''

import sys,heapq
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n,m,party_spot = map(int,input().split())
graph = [ [] for _ in range(n+1) ]
INF = int(21e8)


def dijk(start,end):
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


    res = distance[end]
    return res


for _ in range(m):
    v,w,c = map(int,input().split())
    graph[v].append([w,c])

max_v = -21e8
for start in range(1,n+1):
    Sum = 0
    Sum += dijk(start,party_spot)
    Sum += dijk(party_spot,start)

    if Sum > max_v:
        max_v = Sum

print(max_v)

