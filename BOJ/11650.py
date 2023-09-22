import sys
sys.stdin = open('input.txt','r')

n = int(input())
arr = []
for _ in range(n):
    row = list(map(int,input().split()))
    arr.append(row)


sorted_arr = sorted(arr,key = lambda x: (x[0],x[1]) )

for num in sorted_arr:
    print(*num)