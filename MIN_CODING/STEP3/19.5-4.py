lsts = [[0]*4 for _ in range(4)]

# G: 가로, S: 세로

for _ in range(3):
    line, num = input().split()
    num = int(num)

# 일단 가로 칠하고
# zip(*arr)로 전환? 

    if line == 'G':
        for j in range(4):
            lsts[num][j] = 1
        
    elif line == 'S':
        for i in range(4):
            lsts[i][num] = 1


for lst in lsts:
    print(*lst)