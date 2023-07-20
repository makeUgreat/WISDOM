import sys
sys.stdin = open("input.txt","r")
    
col, row = map(int,input().split())
matrix = []
count = 0
for i in range(row):
    matrix.append(list(input()))
    
for i in range(row):      
    for j in range(col):  
        if matrix[i][j] == '*':
            print('*',end='')
            
        for index_row in range(-1,2): 
            for index_col in range(-1,2):
                if 0 <= i - index_row < row and 0 <= j - index_col < col:
                    if matrix[i-index_row][j-index_col] == '*':
                        count += 1
        
        print(count,end='')
        count = 0   
    print()
    
    

    