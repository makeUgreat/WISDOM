name = ['Amy','Bob','Chloe','Diane','Edger']


matrix = [
    [0,0,0,0,1],
    [1,0,0,0,0],
    [0,1,0,0,0],
    [0,1,0,0,0],
    [0,0,0,0,0]
]
 
max_v = -21e8
max_i = 0
for i in range(len(matrix)):
    cnt = 0
    for j in range(len(matrix[i])):
        if matrix[j][i] == 1:
            cnt += 1
            
    if cnt > max_v:
        max_v = cnt
        max_i = i
    
print(name[max_i])    

        