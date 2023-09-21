import sys
sys.setrecursionlimit(10**9)

import time


start_time = time.perf_counter()

memo = [0]*500000

memo[1] = 1
memo[2] = 2

x = int(input())
for i in range(3,x+1):
    memo[i] = memo[i-1] + memo[i-2]


print(memo[x])

end_time = time.perf_counter()
print(end_time-start_time)