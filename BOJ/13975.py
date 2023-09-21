import sys,heapq
sys.stdin = open('input.txt','r')

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    K = int(input())
    nums = list(map(int,input().split()))

    st_heap = []
    for num in nums:
        heapq.heappush(st_heap,num)

    ans = 0
    while len(st_heap) > 1:
        tmp1 = heapq.heappop(st_heap)
        tmp2 = heapq.heappop(st_heap)
        ans += (tmp1+tmp2)
        heapq.heappush(st_heap,tmp1+tmp2)


    print(ans)
