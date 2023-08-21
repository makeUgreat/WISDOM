import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in (1,T+1):
    N, M = map(int,input().split())

    russia = []
    for _ in range(N):
        row = list(input())
        russia.append(row)

    cnt = 0
    for j in range(M):
        # 가장 첫번째 줄이면서 W가 아닌 값들을 W로 바꾸고 카운트
        if russia[0][j] != 'W':
            russia[0][j] = 'W'
            cnt += 1
    for j in range(M):
        # 가장 마지막 줄이면서 R이 아닌 값들을 R로 바꾸고 카운트
        if russia[N-1][j] != 'R':
            russia[N-1][j] = 'R'
            cnt += 1

    for i in range(1,N-2): # 2번째 줄부터 마지막 바로 윗줄까지
        row_list = []
        for j in range(M):
            row_list.append(russia[i][j])

        print(f'{i}줄 알파벳 {row_list}')

