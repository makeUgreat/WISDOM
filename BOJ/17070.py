import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 1-based graph 생성
N = int(input())
arr = []
for _ in range(N):
    row = list(map(int,input().split()))
    arr.append(row)

# 초기화
memo = [[[-1 for _ in range(4)] for _ in range(N)] for _ in range(N)]

def dfs(p1,p2):

    y1,x1 = p1
    y2,x2 = p2

    if y2==(N-1) and x2==(N-1):
        return 1

    # 파이프
    # 가로방향 -> x2 - x1 = 1, y2 - y1 = 0
    # 세로방향 -> x2 - x1 = 1, y2 - y1 = 1
    # 세로방향 -> x2 - x1 = 0, y2 - y1 = 1
    pipe = 0
    if x2-x1 == 1 and y2-y1 == 0:
        pipe = 1 #가로방향
    elif x2-x1 == 1 and y2-y1 == 1:
        pipe = 2 #대각선
    elif x2-x1 == 0 and y2-y1 == 1:
        pipe = 3 #세로

    if memo[y2][x2][pipe] != -1:
        return memo[y2][x2][pipe]

    total = 0
    diy = [0,1,1]
    dix = [1,1,0]
    for i in range(3):
        dy = y2+diy[i]
        dx = x2+dix[i]

        if dy<0 or dx<0 or dy>=N or dx>=N: continue
        if arr[dy][dx] == 1: continue
        if i == 1: #대각선으로 갈때
            if arr[y2+1][x2] == 1: continue
            if arr[y2][x2+1] == 1: continue

        if pipe == 1: #가로방향일때
            if i == 2: continue
            total += dfs(p2,[dy,dx])

        if pipe == 2: #대각선이면
            total += dfs(p2,[dy,dx])

        if pipe == 3: #세로면
            if i == 0: continue
            total += dfs(p2,[dy,dx])

    memo[y2][x2][pipe] = total
    return total


res = dfs([0,0],[0,1])
print(res)