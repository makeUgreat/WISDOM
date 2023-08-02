lsts_1 = [
    [0,0,0,1],
    [1,1,0,1],
    [1,0,0,1],
    [1,1,1,1]
]

lsts_2 = [
    [1,1,1,1],
    [1,0,1,1],
    [1,0,0,0],
    [1,0,0,0]
]

for i in range(4):
    for j in range(4):
        if lsts_1[i][j] or lsts_2[i][j]:
            lsts_1[i][j] = 1
        else:
            print(f'({i},{j})')
            
