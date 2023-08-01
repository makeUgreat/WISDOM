import sys
sys.stdin = open("for_min_input.txt", "r")

n,x = map(int,input().split())
arr = [ int(i) for i in map(int,input().split()) if i < x]

for i in arr:
    print(i, end=' ')