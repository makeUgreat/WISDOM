import sys
sys.stdin = open('SWEA/input.txt','r')
T = int(input())

for tc in range(1,T+1):

    N = int(input())
    nums = list(map(int,input().split()))

 
    result = sorted(nums)

    print(f'#{tc}',end=' ')
    for i in result:
        print(i,end=' ')
    print()








