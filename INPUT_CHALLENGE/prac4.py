lst=[[1 ,2 ,3 ,4 ,5],
     [2 ,4 ,2 ,1 ,3],
     [3 ,4 ,5 ,2 ,5]]

target = [
    [3,4],
    [2,1]
]

def isPattern(y,x):

    for i in range(2):
        for j in range(2):
            if target[i][j] != lst[y+i][x+j]:
                return 0

    return 1


for i in range(2):       #왜 범위가 1,3?
    for j in range(4):
        ret = isPattern(i,j)
        if ret:
            print(i,j)


