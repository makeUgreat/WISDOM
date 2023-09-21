import sys,heapq,copy
sys.stdin = open('input.txt','r')

N = int(input())
min_heap = []
max_heap = []
arr = []

for _ in range(N):
    arr.append(int(input()))

mid = arr[0]
answer = [mid]

for i in range(1,N):
    num = arr[1]
    if mid <= num:
        heapq.heappush(max_heap,-num)
    else:
        heapq.heappush(min_heap,num)

    print(min_heap)
    print(max_heap)
