arr = [
    [
        ['A','T','B'],
        ['C','C','B']
    ],

    [
        ['A','A','A'],
        ['B','B','C']
    ]

]

st = input()

exist = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(arr[i][j])):
            if arr[i][j][k] == st:
                exist = 1
                break

if exist: print('발견')
else: print('미발견')
