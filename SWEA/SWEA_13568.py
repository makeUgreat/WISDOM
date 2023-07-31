import sys
sys.stdin = open('SWEA/input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())   # N = 배열 길이 M = 이웃하는 수 갯수
    arr = list(map(int,input().split()))

    lsts = []
    for i in range(N):
        sum_ = 0 # 요소 증가할때마다 합 초기화 
        for j in range(M):
            if i+j < N:
                sum_ += arr[i+j]
            else:
                break
        else:
            lsts.append(sum_)
    
    print(f'#{tc} {max(lsts)-min(lsts)}')
    
        
            