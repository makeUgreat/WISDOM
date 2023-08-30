import sys
sys.stdin = open('input.txt','r')

N = int(input())
arr = []
for _ in range(N):
    name,score = input().split()
    arr.append([name,int(score)])
    ans = sorted(arr,key=lambda x: (-x[1], -arr.index(x)))  # 점수가 같으면 나중에 들어온애가 더 앞

    for i in range(min(3,len(ans))): # 상위 3명만 출력할때.. 참고 코드
        print(ans[i][0],end=' ')
    print()




