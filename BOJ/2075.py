# 힙으로 자료구조 저장하고
# 힙팝 5번?
# 메모리초과 -> max값은 항상 마지막줄..

import sys
sys.stdin = open('input.txt','r')

import heapq

N = int(sys.stdin.readline())

st_heap = []
for i in range(N):
    row = list(map(int,input().split()))

    if not st_heap:
        for num in row:
            heapq.heappush(st_heap,num)
    else:
        for num in row:
            if st_heap[0] < num:
                heapq.heappush(st_heap,num)
                heapq.heappop(st_heap)

print(st_heap[0])





