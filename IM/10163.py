import sys
sys.stdin = open('input.txt','r')

Map = [[0]*1002 for _ in range(1002)]

N = int(input())

for num in range(1,N+1):
    x,y,w,h = map(int, input().split())

    for i in range(y,y+h):
        for j in range(x,x+w):
            Map[i][j] = num


for num in range(1,N+1):
    cnt = 0
    # 전체 도화지 순회
    for i in range(1002):
        for j in range(1002):
            if Map[i][j] == num:
                cnt += 1

    print(cnt)



