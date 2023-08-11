
arr = [
    [0 ,0 ,0 ,0 ,0 ,0 ,0],
    [0, 0 ,1, 0 ,1, 0 ,0],
    [0 ,1 ,2 ,0 ,2, 1 ,0],
    [0, 0 ,1 ,2 ,1 ,0 ,0],
    [0 ,0 ,2 ,1 ,0 ,1 ,0],
    [0 ,1 ,1 ,0 ,0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0 ,0 ,0]
]

A, B = map(int, input().split())
arr[A][B] = 1  # 흰돌 착수
answer = 0

directx = [1, -1 ,0, 0]
directy = [0, 0, 1, -1]
for i in range(4):
    dx = A + directx[i]
    dy = B + directy[i]
    if dx > 6 or dx < 0 or dy > 6 or dy < 0 : continue

    bx = 0
    by = 0

    if arr[dx][dy] == 2:
        count = 0
        for j in range(4):
            bx = dx + directx[j]
            by = dy + directy[j]
            if arr[bx][by] == 1:
                count += 1
        if count == 4:
            answer += 1


print(answer)