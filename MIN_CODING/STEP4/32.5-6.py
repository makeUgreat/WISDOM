N,K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
#
# for a in arr:
#     print(*a)
# print()

if K%4 == 1: # 90도 회전
    tmp = arr[::-1]
    ans = list(zip(*tmp))

if K%4 == 2:
    ans = [ row[::-1] for row in arr[::-1] ]


if K%4 == 3:
    tmp = list(zip(*arr))
    ans = tmp[::-1]

if K%4 == 0:
    ans = arr

for a in ans:
    print(*a)
