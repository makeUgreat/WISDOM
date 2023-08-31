arr = [
    ['A','B','C','D'],
    ['A','B','C','E'],
    ['A','G','E','H'],
    ['E','I','E','I'],
    ['F','E','Q','E'],
    ['A','B','A','D'],
]

st = input()

f_idx = []
for i in range(4):
    if st[i] != '?':
        f_idx.append([i,st[i]])

cnt = 0
for i in range(6):
    same = 0
    for j in range(len(f_idx)):
        if arr[i][f_idx[j][0]] != f_idx[j][1]:
            same = 0
        if arr[i][f_idx[j][0]] == f_idx[j][1]:
            same = 1

    if same: cnt += 1

print(cnt)


