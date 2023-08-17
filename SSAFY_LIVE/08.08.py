from collections import deque

name = list(input().split())
arr = [
    [0,1,1,0,0,0],
    [0,0,0,1,1,0],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

# 현재위치 now에서 갈 수 있는 곳을 queue에 다 적기

def bfs(now):
    q = deque()
    q.append(now)
    while q: # q가 비어질 때 까지 반복 
        now = q.popleft()
        print(name[now],end=' ')

        # now 노드가 갈 수 있는 모든 인접노드를 queue에 저장
        for i in range(6):
            if arr[now][i] == 1:
                q.append(i)
    

bfs(0) # 0 -> 탐색 시작 index