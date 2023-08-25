import sys
sys.stdin = open('input.txt','r')

import copy

def continuous(get_arr):
    # 행별, 열별 탐색하면서
    global max_v

    # 행별 탐색
    for i in range(N):
        same = 1
        for j in range(N-1):
            target = get_arr[i][j]
            if get_arr[i][j] == get_arr[i][j+1] == target:
                same += 1
                max_v = max(same,max_v)
            else:
                same = 1

    # 열별 탐색
    rotate = list(zip(*get_arr))
    for i in range(N):
        same = 1
        for j in range(N-1):
            target = rotate[i][j]
            if rotate[i][j] == rotate[i][j+1] == target:
                same += 1
                max_v = max(same,max_v)
            else:
                same = 1


def delta(y,x):
    diy = [-1,1,0,0]
    dix = [0,0,-1,1]


    for i in range(4):
        swaped_arr = copy.deepcopy(arr)
        dy = y + diy[i]
        dx = x + dix[i]

        if dy<0 or dx<0 or dy>N-1 or dx>N-1: continue
        if arr[dy][dx] != arr[y][x]: # 둘이 다른 사탕이면 SWAP
            swaped_arr[dy][dx],swaped_arr[y][x] = swaped_arr[y][x],swaped_arr[dy][dx]
            continuous(swaped_arr)



N = int(input())

arr = []
for _ in range(N):
    row = list(input())
    arr.append(row)


max_v = -21e8


# 모든 배열 순회
for i in range(N):
    for j in range(N):
        # 상하좌우 탐색 및 다르면 스왑 
        delta(i,j)
        
print(max_v)
