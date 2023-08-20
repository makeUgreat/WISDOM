import sys
sys.stdin = open('SWEA/input.txt')

T = int(input())

def IsSame(get_arr):
    '''
    배열을 탐색하면서 저장하다가
    탐색할 값이 저장되었던 값이면 중복으로 나온 값이므로 
    flag를 0으로 설정한다
    '''
    global flag
    save_num = []

    for num in get_arr:
        if num in save_num:
            flag = 0
            break
            
        save_num.append(num)
     

def IsSame_square(get_arr,y,x):
    global flag
    save_num = []
    
    for i in range(3):
        for j in range(3):
            if get_arr[y+i][x+j] in save_num:
                flag =0
                break
            save_num.append(get_arr[y+i][x+j])


for tc in range(1,T+1):
    
    puzzle = []
    for _ in range(9):
        row = list(map(int,input().split()))
        puzzle.append(row)

    flag = 1


    # 가로줄 체크
    for i in range(9):
        IsSame(puzzle[i]) 
        
    # 세로줄 체크
    for col in zip(*puzzle):
        IsSame(col)
        
    # 3*3 정사각형 체크

    for i in range(0,7,3):
        for j in range(0,7,3):
            IsSame_square(puzzle,i,j)
            

    if flag:
        result = 1
    else:
        result = 0
        
    print(f'#{tc} {result}')
        