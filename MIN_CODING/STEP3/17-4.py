lsts = [
    ['A','T','K','B'],
    ['C','Z','F','D'],
    ['H','G','E','I']
]

ch1, y, x = input().split()
x = int(x)
y = int(y)

offset_x = 0
offset_y = 0

for i in range(len(lsts)):
    for j in range(len(lsts[i])):

        if lsts[i][j] == ch1:
            offset_x = j+x
            offset_y = i+y


print(lsts[offset_y][offset_x])


