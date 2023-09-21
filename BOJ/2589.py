from collections import deque
import sys
sys.stdin = open('input.txt','r')

# 육지를 찾기 위해 전체 배열 탐색을 돌린다
# 육지를 발견하면 BFS 탐색을 한다
# 탐색하면서 대륙의 위치정보를 따로 저장한다 -> 배열에
# 저장한 위치정보마다 출발지로 정해서 다시 bfs탐색을 돌린다
# 이 과정에서 cnt의 최대값이 되는 경우 갱신해주고 동시에 위치도 저장한다(시작,끝)

# 위 과정을 완료한 대륙은.. 다시 탐색하지 않도록 W처리한다
# -> 저장한 위치정보를 이용하여 모두 W로 바꿔준다

# 다음 대륙으로 넘어가기 위해 전체 배열 탐색을 돌린다-> 반복

def save_land_data(i,j):
    global land_data
    visit = [[False]*M for _ in range(N)]
    q = deque()
    q.append([i,j])
    visit[i][j] = True
    land_data.append([i,j])

    while q:
        y,x= q.popleft()

        diy = [-1,1,0,0]
        dix = [0,0,-1,1]
        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]

            if dy<0 or dx<0 or dy>=N or dx>=M: continue
            if visit[dy][dx]: continue
            if arr[dy][dx] == 'W': continue

            visit[dy][dx] = True
            q.append([dy,dx])
            land_data.append([dy,dx])


def bfs(yy,xx):
    global max_i, max_j,Max
    visit = [[False]*M for _ in range(N)]

    q2 = deque()
    q2.append([yy,xx,0])
    visit[yy][xx] = True

    while q2:
        y,x,cnt = q2.popleft()

        diy = [-1,1,0,0]
        dix = [0,0,-1,1]
        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]

            if dy<0 or dx<0 or dy>=N or dx>=M: continue
            if visit[dy][dx]: continue
            if arr[dy][dx] == 'W': continue


            visit[dy][dx] = True
            q2.append([dy,dx,cnt+1])

            if cnt+1 > Max:
                Max = cnt+1
                max_i = dy
                max_j = dx

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]


land_data = []
max_i = -1
max_j = -1
Max = -21e8
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L': # 육지면
            # print('--------------')

            # for a in arr:
            #     print(*a, sep='')
            save_land_data(i,j)

            for yy,xx in land_data:
                bfs(yy,xx)
            # print(f'최대값 좌표: {max_i},{max_j},최대값: {Max}')

            for yy,xx in land_data:
                arr[yy][xx] = 'W'

            land_data.clear()

print(Max)


