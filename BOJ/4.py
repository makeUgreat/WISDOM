import sys
sys.stdin = open('input.txt','r')

import time
N,K = map(int,input().split())

cnt = 0
start_time = time.perf_counter()
while N > 1:
    if N % K == 0 and N/K >= 1:
        N /= K
    else:
        N -= 1

    cnt += 1

end_time = time.perf_counter()
print(cnt)

print("time: ", end_time - start_time)