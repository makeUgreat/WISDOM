N = int(input())

# 인덱스번호,움직일 위치(인덱스+)
foot = [
    [0,3],
    [1,2],
    [2,-1],
    [3,3],
    [4,-2],
    [5,0],
    [6,-1]
]

def abc(idx):

    if idx == 5:
        print(f'{idx}번')
        return

    abc( idx + foot[idx][1] )
    print(f'{idx}번')

abc(N)