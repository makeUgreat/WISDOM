Map = [
    [3,5,1],
    [3,8,1],
    [1,1,5]
]

bitarray = []
for _ in range(2):
    line = list(map(int,input().split()))
    bitarray.append(line)


def masking(y,x):
    Sum = 0
    for i in range(2):
        for j in range(2):
            if bitarray[i][j] == 1:
                Sum += Map[i+y][j+x]

    return Sum




max_sum = -21e8
max_i = 0
max_j = 0
for i in range(2):
    for j in range(2):
        if masking(i,j) > max_sum:
            max_sum = masking(i,j)
            max_i = i
            max_j = j

print(f'({max_i},{max_j})')