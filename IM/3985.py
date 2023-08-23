import sys
sys.stdin = open('input.txt','r')

L = int(input())
N = int(input())


roll = [0]*(L+1)
max_v = -21e8
max_i = 0
for i in range(1,N+1):
    P,K = map(int, input().split())

    # 가장 많이 받을 것으로 기대하던 방청객
    if K-P > max_v:
        max_v = K-P
        max_i = i

    for j in range(P,K+1):
        if roll[j] == 0:
            roll[j] = i


# 실제로 가장 많이 받은 방청객

max_cnt = -21e8
real_max = []

for i in range(1,N+1):
    cnt = 1

    for k in range(len(roll)-1):
        if roll[k] == roll[k+1] == i:
            cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt
        real_max = i


print(max_i)
print(real_max)