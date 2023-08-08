def Boom(y,x):
    
    direction = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    
    for dyt, dxt in direction:
        dy = y + dyt
        dx = x + dxt 
        if dx<0 or dy<0 or dx>4 or dy>3: continue
        arr[dy][dx] = '#'
    


arr = [['_'] * 5 for _ in range(4)]


for _ in range(2):
    y,x = map(int,input().split())

    Boom(y,x)

for a in arr:
    print(*a)