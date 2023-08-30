n,m = map(int,input().split()) # 정점갯수, 간선갯수
lst = [list(input().split()) for _ in range(m)]
parent = [0] * 200

lst.sort(key=lambda x:int(x[2])) # 가중치 순으로 정렬
def findP(node):
    if not parent[ord(node)]: # 부모정보가없으면
        return node  # 그 노드가 부모

    # 부모 있으면 그 부모로 재귀탐색
    res = findP(parent[ord(node)])
    parent[ord(node)] = res
    return res

def union(x,y,i):
    global parent,total,cnt
    x_parent, y_parent = findP(x),findP(y)
    if x_parent == y_parent:
        return
    cnt += 1
    total += int(lst[i][2]) # 비용 추가
    parent[ord(y_parent)] = x_parent



total = 0 # 공사비용
cnt = 0   # 연결시킨 선의 갯수

for i in range(m): # 간선을 탐색하면서
    if cnt == n-1: # 간선의 갯수는 정점갯수 - 1 이여야 신장트리이므로
        print(total)
        break
    union(lst[i][0],lst[i][1],i)

