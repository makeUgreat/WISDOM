import sys
sys.stdin = open('input.txt','r')

N,K = map(int,input().split())
res = 0

while 1:
    target = (N//K) * K
    res += (N-target)
    N = target

    if N < K:
        break

    res += 1
    N //= K


res += (N-1)

print(res)
