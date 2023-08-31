arr = [
    ['A','B','C','E','F','G'],
    ['H','I','J','K','L','M'],
    ['N','O','P','Q','R','S']
]

arr_backup = [
    ['A','B','C','E','F','G'],
    ['H','I','J','K','L','M'],
    ['N','O','P','Q','R','S']
]

def delta(y,x):
    diy = [0,-1,1,0,0]
    dix = [0,0,0,-1,1]

    for i in range(5):
        dy = y + diy[i]
        dx = x + dix[i]

        if dy<0 or dx<0 or dy>2 or dx>5: continue
        if arr[dy][dx] == '#':
            arr[dy][dx] = arr_backup[dy][dx]

        else:
            arr[dy][dx] = '#'


st = list(input())

for target in st:

    for i in range(3):
        for j in range(6):
            if arr[i][j] == target:
                delta(i,j)

for a in arr:
    print(*a,sep='')

