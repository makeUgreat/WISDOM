import sys
sys.stdin = open('input.txt','r')

n = int(sys.stdin.readline())
bucket = [0] * (10001)
for _ in range(n):
    bucket[int(sys.stdin.readline())] += 1

for i in range(10001):
    if bucket[i] != 0:
        for __ in range(bucket[i]):
            print(i)

