import sys
sys.stdin = open("MIN_CODING/STEP3/input.txt","r")


def make_arr():
    
    tmp_arr = []
    for _ in range(4):
        line = list(map(int,input().split()))
        tmp_arr.append(line)
    
    return tmp_arr


arr_A = make_arr()
empty = input()
arr_B = make_arr()

flag = 0 
for i in range(4):
    for j in range(4):
        if arr_A[i][j] == arr_B[i][j] == 1:
            flag = 1

if flag: print('걸리다')
else: print('걸리지않는다')