import sys, copy
sys.stdin = open('input.txt','r')

N = int(input())

# 그래프 만들기
graph = [ [] for _ in range(N+1)]
# 인덱스 순이 아닌 값 순으로 인접리스트를 만든 이유?
# 오히려 1~N 까지 각 숫자마다 순회하면서 찾기 위해서는 반대로 연결해야함
# ex) 인덱스 순이면 2와 3인덱스를 볼때 1과 연결되었음을 알 수 있지만 반대로 연결하면
# 1인덱스를 보면 2,3이 연결되었음을 알 수 있음

for i in range(1,N+1):
    graph[int(input())].append(i)

visit = [False] * (N+1)
result =[]


def dfs(node,route):
    route.add(node) #방문경로 기록

    visit[node] = True
    for next in graph[node]:
        if next not in route:
            dfs(next, route.copy()) # 재귀로 들어갔을 때 새로운 배열을 참조하는 것이 아니라 같은 route를 참조하도록 얕은 복사
        else: # 방문했었던 노드라면 처음 노드로 되돌아온것이므로
            result.extend(list(route)) # 결과에 현재까지의 기록 저장
            return


for i in range(1,N+1):
    if not visit[i]:
        dfs(i,set())

result.sort()
print(len(result))
for num in result:
    print(num)