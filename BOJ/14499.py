import sys
sys.stdin = open('input.txt','r')

n,m,x,y,k = map(int,input().split())
arr = []
for _ in range(n):
    row = list(map(int,input().split()))
    arr.append(row)

orders = list(map(int,input().split()))

'''
#1 시작위치에서 주사위를 굴린다
#2 이 때 굴리는 방향에 따라 바닥이 되는 위치를 바꿔준다
#3 굴린 위치의 지도가 0이라면 -> 바닥면 값을 지도에
#4 0이 아니라면 -> 지도값을 바닥면에 복사하고 지도의 값을 0으로 초기화
#5 그리고 이 때 주사위 상단에 쓰인 값을 출력한다

'''
dice= [0,0,0,0,0,0]

# 동(1) - 서(2) - 북(3) -  남(4)
dix = [0,0,0,-1,1]
diy = [0,1,-1,0,0]

for order in orders:
    dy = y + diy[order]
    dx = x + dix[order]
    if dy<0 or dx<0 or dy>=m or dx>=n: continue

    # 갈 수 있으면 조건 변경
    # 주사위 바닥 인덱스 변경
    # 주사위 0번부터
    # 동서남북 위 아래
    E = dice[0]
    W = dice[1]
    S = dice[2]
    N = dice[3]
    up = dice[4]
    down = dice[5]

    # 윗면은 굴리는 방향으로 변경/ 아랫면은 그 반대방향
    # 동,서로 굴리면 북,남 고정
    # 북,남으로 굴리면 동,서 고정
    if order == 1: #동
        dice[0], dice[1], dice[4], dice[5] = down, up, E, W
    elif order == 2: #서
        dice[0], dice[1], dice[4], dice[5] = up, down, W, E
    elif order == 3: #북
        dice[2], dice[3], dice[4], dice[5] = up, down, N, S
    elif order == 4: #남
        dice[2], dice[3], dice[4], dice[5] = down, up, S, N


    if arr[dx][dy] == 0:  #이동할 칸의 맵이 0이면
        arr[dx][dy] = dice[5] #맵에 주사위 아랫면 값 붙여넣기

    else: # 0이 아니면
        dice[5] = arr[dx][dy] # 맵의 값을 주사위에 붙여넣기
        arr[dx][dy] = 0

    y,x = dy,dx
    print(dice[4])


