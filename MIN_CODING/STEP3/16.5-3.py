line = list(map(int,input().split()))
lsts = [[0] * 3 for _ in range(2) ]

max_v = max(line)
min_v = min(line)

for i in range(2):
    for j in range(3):
        lsts[i][j] = line[i * 3 + j]
        if lsts[i][j] == max_v:
            print(f'({i},{j})')
        elif lsts[i][j] == min_v:
            print(f'({i},{j})')

