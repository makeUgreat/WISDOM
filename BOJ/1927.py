import heapq
import sys
sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline())
st_heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if st_heap:
            print(heapq.heappop(st_heap))
        else:
            print(0)

    else:
        heapq.heappush(st_heap,x)

