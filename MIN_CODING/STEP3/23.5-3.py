array = [[0 for _ in range(4)] for _ in range(4)]

# 3x3 숫자 입력받기
for i in range(3):
    row = list(map(int, input().split()))
    for j in range(3):
        array[i][j] = row[j]
        
        
for i in range(3):
    for j in range(3):
        array[i][3] += array[i][j] #가로줄 합 
        array[3][j] += array[i][j] # 세로줄 합
    
        if i == j:
            array[3][3] += array[i][j]
            
        
for arr in array:
    print(*arr)