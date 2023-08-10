import sys
sys.stdin = open("SWEA/input.txt","r")


def flapFlysum(y,x):
    sum_ = 0
    for i in range(m):
        for j in range(m):
            sum_ += lsts[i+y][j+x] 
    return sum_

T = int(input())

for tc in range(1,T+1):
    
    n, m = map(int,input().split()) 
    # 배열 크기 n*n
    # 파리채 크기 m*m
    
    # 배열 생성
    lsts = []
    for i in range(n):
        line = list(map(int,input().split()))
        lsts.append(line)

    # 파리채로 배열 내려쳤을 때 잡은 파리수 찾기
    # (m-n)+1 => 배열이 m개이고  파리채 크기가 n개일 때 
    # 파리채가 전체를 다 탐색하려면 필요한 횟수 (정사각형)
    max_v = -21e8
    for i in range( (n-m)+1 ):
        for j in range( (n-m)+1 ):
            if max_v < flapFlysum(i,j):
                max_v = flapFlysum(i,j)
            
    print(f'#{tc} {max_v}')