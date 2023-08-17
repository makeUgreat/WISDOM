from collections import deque

arr = [
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0],
    [1,0,1,0,0],
    [1,0,0,0,1]
]
 
size_list = []
def bfs(y,x):

    q = deque()
    q.append([y,x])
    size = 1
    arr[y][x] = 0

    while q:
        directy = [-1,1,0,0]
        directx = [0,0,-1,1]

        yy,xx = q.popleft()

        for i in range(4):
            dy = yy+directy[i]
            dx = xx+directx[i]

            if dy<0 or dx<0 or dy>=5 or dx>=5: continue
            if arr[dy][dx] == 1:
                q.append([dy,dx])
                arr[dy][dx] = 0
                size += 1
    
    return size

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            size_list.append(bfs(i,j))

print(len(size_list))
print(max(size_list))
print(min(size_list))

