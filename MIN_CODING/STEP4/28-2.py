branch = int(input())

matrix = [] 
for _ in range(branch):
    line = list(map(int,input().split()))
    matrix.append(line)
    

root = 0
leaf = []
for i in range(len(matrix)):
    Sum = 0
    for j in range(len(matrix[i])):
        Sum += matrix[j][i] 
    
    if Sum == 0:
        root = i

cnt = 0
for j in range(branch):
    if matrix[0][j] == 1:
        leaf.append(j)


result = ' '.join(map(str,leaf))

print(f'boss:{root}')
print(f'under:{result}')
