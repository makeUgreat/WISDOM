import sys
sys.stdin = open('input.txt','r')

N = int(input()) # 컴퓨터의 수 (정점의 수)
M = int(input()) # 연결할 수 잇는 선의 수 (간선의 수)

# 최소신장트리 구현해서 풀기
# 간선의 정보 입력받기
edge = []
for _ in range(M):
    edge.append(list(map(int,input().split())))

# 비용을 기준으로 오름차순 정렬하기
edge.sort(key=lambda x: x[2])

parent = [0] * (N+1)

def findP(get_node):
    if parent[get_node] == 0: # 해당 노드의 부모정보가 없으면
        return get_node # 부모는 해당 노드

    # 해당 노드의 부모 정보가 있으면 부모 노드의 부모를 찾기위해 깊은 탐색
    res = findP(parent[get_node])
    return res # 부모 정보 반환


def union(x,y,c):
    # 두 정점을 같은 그룹으로 묶는 함수
    global parent,cost
    # 묶기 위해서 먼저 두 노드의 부모 노드를 체크
    xP = findP(x)
    yP = findP(y)
    # 만약 두 x,y 정점의 가장 마지막 부모 노드가 같다면 싸이클이니까 합치지않고 리턴
    if xP == yP:
        return

    # 싸이클이 아니라면(루트노드가 다르면)
    cost += c # 해당 간선이 추가되니까 비용추가
    parent[yP] = xP # 두 부모끼리 같은 그룹임을 명시


# 정렬된 간선 리스트 중 순서대로(비용이 낮은 순으로) 선택한다
cost = 0
for i in range(M):
    v,w,c = edge[i]
    union(v,w,c)

print(cost)
