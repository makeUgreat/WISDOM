lsts = []

for _ in range(4):
    line = list(input())
    lsts.append(line)


memo_i = 0
memo_j = 0
for i in range(len(lsts)):
    for j in range(len(lsts[i])):
        if lsts[i][j] == 'A':
            memo_i = i
            memo_j = j 
            break
track = 0
for i in range(len(lsts)):
    for j in range(len(lsts[i])):
        if lsts[i][j] == 'B':
            track += abs(memo_i - i)
            track += abs(memo_j - j)

print(track)