import sys
sys.stdin = open('input.txt','r')

import heapq

N = int(sys.stdin.readline())
st_heap = []
for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if not st_heap:
            print(0)
        else:
            print(-heapq.heappop(st_heap))

    else:
        heapq.heappush(st_heap,-x)


