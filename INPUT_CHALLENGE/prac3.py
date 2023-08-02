'''
1 2 3 4 5
2 4 2 1 3
3 4 5 2 5

3 4 5 라는 패턴이 어느 좌표에 있는지 찾기!!

정답은:
0 2
2 1
'''

lsts = [
    [1,2,3,4,5],
    [2,4,2,1,3],
    [3,4,5,2,5]
]

target = [3,4,5]
def isPattern(y,x):
    for i in range(3):
        if target[i] != lsts[y][x+i]:
            return 0

    return 1

for i in range(3):
    for j in range(3):
        ret = isPattern(i,j)
        if ret:
            print(i,j)
