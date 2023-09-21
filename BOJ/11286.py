import sys,heapq
sys.stdin = open('input.txt','r')


N = int(sys.stdin.readline())
st_heap = []
lst = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if not st_heap:
            print(0)
        else:
            print(heapq.heappop(st_heap)[1])
    else:
        heapq.heappush(st_heap, (abs(x),x))