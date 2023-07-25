lsts = [
    ['D','A','A'],
    ['B','C','D'],
    ['E','F','A'],
    ['A','A','D'],
    ['F','G','E']
]

ch1 = input()

for i in range(len(lsts)):
    for j in range(len(lsts[i])):
        if lsts[i][j] == ch1:
            print(f'({i},{j})')


