from copy import deepcopy

arr = [
    [6,4,7],
    [3,3,1],
    [9,5,8]
]

arr2 = [
    [6,4,7],
    [3,3,1],
    [9,5,8]
]

direction = [ (0,0),(-1,0),(1,0),(0,1),(0,-1)]
visit = [[0]*3 for _ in range(3)]


def dfs(y,x,level):
    Sum = 0
    if level == 0:
        for row in arr:
            for j in row:
                Sum += j  
        

    if level == 3:
        return Sum
    
    for yy,xx in direction:
        dy = y + yy
        dx = x + xx 

        if dy<0 or dx<0 or dy>2 or dx>2: continue
        arr[dy][dx] = (arr[dy][dx]*7) % 10

dfs(1,1,1)
print(arr)
