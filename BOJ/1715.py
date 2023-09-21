import sys,heapq
sys.stdin = open('input.txt','r')

N = int(input())
st_heap = []
for _ in range(N):
    heapq.heappush(st_heap,int(input()))

ans = 0
while len(st_heap) > 1:
    tmp1 = heapq.heappop(st_heap)
    tmp2 = heapq.heappop(st_heap)
    ans += (tmp1+tmp2)
    heapq.heappush(st_heap,tmp1+tmp2)

print(ans)