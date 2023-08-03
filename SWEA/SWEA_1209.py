import sys
sys.stdin = open("input.txt","r")

T = 10
for tc in range(1,T+1):

    row_sum = 0
    col_sum = 0
    diag_sum = 0

    lsts = [list(map(int,input().split())) for _ in range(100)]

    for i in range(len(lsts)):
        for j in range(len(lsts[i])):

            col_sum += lsts[i][j]
            row_sum += lsts[j][i]
        diag_sum += lsts[i][i]
