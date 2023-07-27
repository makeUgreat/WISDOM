lsts = [
    ['a','b','E'],
    ['E', 2, 'W'],
    [ 3,  2,  4 ]
]


for i in range(len(lsts)):
    for j in range(len(lsts[i])):
        if type(lsts[i][j]) == str:
            if lsts[i][j].islower():
                lsts[i][j] = lsts[i][j].upper()
            elif lsts[i][j].isupper():
                lsts[i][j] = lsts[i][j].lower()
        else:
            lsts[i][j] += 5

for lst in lsts:
    print(*lst)
