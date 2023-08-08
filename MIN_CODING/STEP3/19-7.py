
input_arr = []
for _ in range(4):
    line = list(map(int,input().split()))
    input_arr.append(line)
    
vect = [ [0]*3 for _ in range(4)]

for i,j in input_arr:
    vect[i][j] = 5

for v in vect:
    print(*v)