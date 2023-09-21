import sys,heapq,copy
sys.stdin = open('input.txt','r')

input = sys.stdin.readline

N,L = map(int,input().split())  # L만큼 슬라이딩 윈도우
D = list(map(int,input().split()))

# L만큼의 슬라이딩 윈도우를 하는데 그 중 최솟값을 뽑을꺼니까 -> Min heap으로 구성
# 흠.. ...... Min heap을 만들되 L만큼의 자료만 들어오게 만들면 될 듯 ?

st_heap = []
window = [D[0]]
# 뽑고 출력 -> 뽑은거 다시 저장
for i in range(1,N+1):
    tmp = copy.deepcopy(window)
    heapq.heapify(tmp)
    print(tmp)
    print(heapq.heappop(tmp),end=' ')

    if len(window) >= L:
        window.pop(0)
    if i < N:
        window.append(D[i])
