import sys
sys.stdin = open("SWEA/input.txt","r")

T = 10
for tc in range(1,T+1):

    tc_num = int(input())
    
    arr = []
    # 100*100 배열 생성
    for _ in range(100):
        line = list(map(int,input().split()))
        arr.append(line)
    
    
    col_sum_list = []
    row_sum_list =[]
    ex_diag_sum = 0
    diag_sum = 0
    for col in arr:
        col_sum_list.append(sum(col))
    
    
    for row in zip(*arr):
        row_sum = sum(row)
        row_sum_list.append(row_sum)
        
    for i in range(100):
        diag_sum += arr[i][i]
    
    for i in range(100):
        ex_diag_sum += arr[i][100-1-i]

    max_list = []
    max_list.append(max(col_sum_list))
    max_list.append(max(row_sum_list))
    max_list.append(diag_sum)
    max_list.append(ex_diag_sum)
    
    print(f'#{tc_num} {max(max_list)}')
    
    
