import sys
sys.stdin = open('input.txt','r')

arr = []
for _ in range(5):
    row = list(map(int,input().split()))
    arr.append(row)

call = []
for _ in range(5):
    row = list(map(int,input().split()))
    call.append(row)

def wherearr(value):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == value:
                return i,j

def count(arr):
    bingo_cnt = 0
    zero_cnt = 0
    zero2_cnt = 0

    rotate_arr = list(zip(*arr))
    for i in range(5):
        # 가로줄 체크
        if arr[i].count(0) == 5:
            bingo_cnt += 1
        # 세로줄 체크
        if rotate_arr[i].count(0) == 5:
            bingo_cnt += 1

        # 왼우 대각선 체크
        if arr[i][i] == 0:
            zero_cnt += 1

        # 우왼 대각선 체크
        if arr[i][4-i] == 0:
            zero2_cnt += 1

        if zero_cnt == 5:
            bingo_cnt += 1
        if zero2_cnt == 5:
            bingo_cnt += 1

    if bingo_cnt >= 3:
        return 1
    return 0



min_v = 21e8
cnt = 0
flag = 1
if flag:
    for i in range(5):
        if flag:
            for j in range(5):
                y,x = wherearr(call[i][j])
                arr[y][x] = 0
                cnt += 1
                # print(f'{cnt}번 착수:')
                if count(arr):
                    print(cnt)
                    flag =0
                    break
        # for a in arr:
        #     print(*a)







