lsts = []
for _ in range(4):
    line = list(input())
    lsts.append(line)

row_lsts = []
for lst in zip(*lsts):
    row_lsts.append(list(lst))


for _ in range(3):
    for row in row_lsts:
        for i in range(3):
            # if row[i] == '_':
            #     continue

            # if row[i+1] == '_':
            #     row[i+1] = row[i]
            #     row[i] = '_'
            
            if row[i] != '_' and row[i+1] == '_':
                row[i+1] = row[i]
                row[i] = '_'


for maps in zip(*row_lsts):
    print(*maps,sep='')