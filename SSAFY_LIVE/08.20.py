
# 위 아래 좌 우로 3칸까지 떨어진 곳들의 합을 구하기
# 2 2 입력시  18 가 출력이 됩니다. # (4+2+4+2+1+2+1+2=18)
# 0 0 입력시  19 가 출력이 됩니다. # (1+1+3+5+4+5=19)
# 3 4 입력시  38 이 출력이 됩니다. # (6+8+2+5+4+5+8=38)

arr = [ [3, 5, 4, 5, 6],
        [1, 1, 2, 7, 8],
        [1, 2, 9, 1, 2],
        [3, 5, 4, 5, 6],
        [1, 1, 2, 7, 8]]

y,x=map(int,input().split())
directy=[-1,1,0,0]
directx=[0,0,-1,1]

Sum = 0
for i in range(4):
    for j in range(1,4):
        dy = y + (directy[i] * j)
        dx = x + (directx[i] * j)
        
        if dy<0 or dx<0 or dy>=5 or dx>=5: continue
        Sum += arr[dy][dx]
        
print(Sum)
        