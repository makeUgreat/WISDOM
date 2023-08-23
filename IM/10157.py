C,R = map(int, input().split()) # 가로 세로

Map = [ [0] * (C+1) for _ in range(R+1) ]  # 인덱스를 위해 한 줄씩 추가



diry = [-1,1,0,0]
dirx = [0,0,-1,1]

y = 1
x = 1
num = 1

while 1:
    if num >= C*R:
        break

    for i in range(4):
        dy = y + diry[i]
        dx = x + dirx[i]

        if dy < 1 or dx < 1 or dy > R+1 or dx > C+1: continue
        if Map[dy][dx] != 0: continue
        Map[dy][dx] = num
        num += 1
        break


for m in Map:
    print(*m)




