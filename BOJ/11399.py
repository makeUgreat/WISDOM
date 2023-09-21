import sys
sys.stdin = open('input.txt','r')

N = int(input())
times = list(map(int,input().split()))
times.sort()

Sum = 0
for i in range(1,N+1):
    Sum += sum(times[0:i])

print(Sum)