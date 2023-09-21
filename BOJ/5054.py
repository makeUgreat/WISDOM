import sys
sys.stdin = open('input.txt','r')

t = int(input())

for _ in range(t):
    n = int(input())
    position = list(map(int,input().split()))
    position.sort()


    ans = (position[-1] - position[0]) * 2
    print(ans)
