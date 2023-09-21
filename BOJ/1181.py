import sys
sys.stdin = open('input.txt','r')

N,L = map(int,input().split())
arr = [[0,0,1]]
for _ in range(N):
    D,R,G = map(int,input().split())
    arr.append([D,R,G])

arr.append([L,0,1])

time = 0
for i in range(1,len(arr)):
    d,r,g = arr[i]
    time += d - arr[i-1][0] # 이전 시간의 d는 제외(현재위치까지의 d만 고려)
    wait = r - (time % (r+g))
    time += max(0,wait)

print(time)



