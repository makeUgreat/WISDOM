import sys
sys.stdin = open('input.txt','r')

arr = [list(map(int,input().split())) for _ in range(4) ]

for a in arr:
    print(*a)