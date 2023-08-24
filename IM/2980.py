import sys

sys.stdin = open('input.txt', 'r')

N, L = map(int, input().split())
arr = [[0,0,1]]

for i in range(N):
    D, R, G = map(int, input().split())  # 신호등 위치, 초록,빨강불
    arr.append( [D,R,G] )

arr.append( [L,0,1] )

time = 0
for i in range(1, len(arr)):
    d,r,g = arr[i]
    time += d - arr[i-1][0]
    wait = r - (time % (r + g))
    time += max(0,wait)


print(time)


