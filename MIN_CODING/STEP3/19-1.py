arr = [
    [3,5,4],
    [1,1,2],
    [1,3,9]
]

y,x = map(int,input().split())

directx = [-1,1,0,0]
directy = [0,0,-1,1]

Sum = 0
for dtx,dty in zip(directx,directy):
    dx = x + dtx
    dy = y + dty 
    if dx<0 or dy<0 or dx>2 or dy>2:
        continue
    Sum += arr[dy][dx] 

print(Sum)