import heapq
import sys
sys.stdin = open('input.txt','r')

N = int(input())
for _ in range(N):
    x = int(input())
    st_heap = []
    if x == 0:
        if not st_heap:
            print(0)
        else:
            print(heapq.heappop(st_heap))

    heapq.heappush(st_heap,x)