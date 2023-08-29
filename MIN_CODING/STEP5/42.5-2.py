arr = [ list(input()) for _ in range(4) ]
# visit = [[False]*4 for _ in range(4)]
N = int(input())
char = ['A','B','C','D','E','F','G','H','I']


def bomb(y,x):
    cnt = 0
    diy = [0,-1,1,0,0]
    dix = [0,0,0,-1,1]

    for i in range(5):
        dy = y + diy[i]
        dx = x + dix[i]

        if dy<0 or dx<0 or dy>3 or dx>3: continue
        if arr[dy][dx] not in char: continue

        arr[dy][dx] = 0

    return cnt


bomb_list = []
for i in range(4):
    for j in range(4):
        if arr[i][j] in char:
            res = bomb(i,j)
            bomb_list.append([res,arr[i][j]])

bomb_list.sort(key=lambda x: (-x[0],x[1]))
print(bomb_list)