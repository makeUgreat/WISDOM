import sys
sys.stdin = open('input.txt','r')

def move(get_order,y,x):
    # 맵이 거꾸로니까
    # 위로 올라갈때는.. y+1
    # 아래로 내려갈때는 .. y-1
    dy,dx = 0,0

    if get_order == 'R':
        dy = y
        dx = x+1
    if get_order == 'L':
        dy = y
        dx = x-1
    if get_order == 'B':
        dy = y+1
        dx = x
    if get_order == 'T':
        dy = y-1
        dx = x
    if get_order == 'RT':
        dy = y-1
        dx = x+1
    if get_order == 'LT':
        dy = y-1
        dx = x-1
    if get_order == 'RB':
        dy = y+1
        dx = x+1
    if get_order == 'LB':
        dy = y+1
        dx = x-1

    # 범위를 벗어나면 움직이지않게 기존 좌표를 넘김
    if dy <0 or dx <1 or dy > 7 or dx> 8:
        return y,x
    else:
        return dy,dx

Map = [[0]*9 for _ in range(9)]
row = [8,7,6,5,4,3,2,1,0]
col = ['','A','B','C','D','E','F','G','H']

king, stone, N = input().split()
N = int(N)
# 상하가 반대로니까..
# 따라서 마지막에 좌표 출력할때도 상하 반대로..
king_x,king_y = col.index(king[0]), row.index(int(king[1]))
stone_x,stone_y = col.index(stone[0]), row.index(int(stone[1]))

# 왕의 첫 위치
Map[king_y][king_x] = 1
# 돌의 첫 위치
Map[stone_y][stone_x] = 2

for _ in range(N):
    order = input()
    k_flag = 1
    kyy,kxx = king_y,king_x  # 움직이기 전 위치 저장
    syy,sxx = stone_y,stone_x

    # 왕 좌표 수정
    king_y, king_x = move(order,king_y,king_x)

    # 움직이려는 위치에 돌이 있으면 돌도 같은 방향으로 움직이고
    # 돌이 더 이상 움직일 수 없는 위치에 있으면 밀던 킹의 좌표도 원래 좌표로 고정한다.
    if Map[king_y][king_x] == 2: # 움직였더니 돌이있음
        # 우선, 돌도 해당 방향으로 움직여본다
        stone_y, stone_x = move(order,stone_y,stone_x)
        # 만약 움직이지 않았으면(함수 전,후 좌표가 같으면)
        if stone_y == syy and stone_x == sxx:
            # 돌이 더이상 움직일 수 없으니 킹도 가만히 둔다
            king_y,king_x = kyy, kxx
            # 왕이 움직이지 않으면 0으로 바꾸지 않기 위해 플래그
            k_flag = 0

        else: # 움직일 수 있으면(함수, 전후 좌표가 다르면)
            Map[stone_y][stone_x] = 2 # 돌 이동

    # 왕 움직임
    Map[king_y][king_x] = 1
    if k_flag:
        Map[kyy][kxx] = 0


# 돌 위치 구하기
k_i = 0
k_j = 0
s_i = 0
s_j = 0
for i in range(9):
    for j in range(9):
        if Map[i][j] == 1:
            k_i = i
            k_j = j
        if Map[i][j] == 2:
            s_i = i
            s_j = j

for m in Map:
    print(*m)
print(f'{col[k_j]}{row[k_i]}')
print(f'{col[s_j]}{row[s_i]}')


