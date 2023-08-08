def sumDiag(y,x):
    Sum = 0
    direction = [(-1,-1),(-1,1),(1,-1),(1,1)] # 대각선
    
    for dyt,dxt in direction:
        dy = y + dyt
        dx = x + dxt
        if dx<0 or dy<0 or dx>4 or dy>4: continue
        Sum += my_map[dy][dx]
    
    return Sum


my_map = [
    [3,3,5,3,1],
    [2,2,4,2,6],
    [4,9,2,3,4],
    [1,1,1,1,1],
    [3,3,5,9,2]
]

max_Sum = 0
max_y = 0
max_x = 0
for y in range(len(my_map)):
    for x in range(len(my_map[y])):
        if sumDiag(y,x) > max_Sum:
            max_Sum = sumDiag(y,x)
            max_y = y
            max_x = x

print(max_y,max_x)