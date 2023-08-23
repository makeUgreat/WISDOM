import sys
sys.stdin = open('input.txt','r')

Map = [[0]*101 for _ in range(101)]
N = int(input()) # 종이 갯수

for _ in range(N):
    x,y = map(int, input().split()) 
    

    for i in range(y,y+10):
        for j in range(x,x+10):
            Map[i][j] = 1

directy = [-1,1,0,0]
directx = [0,0,-1,1]

cnt = 0
for i in range(100):
    for j in range(100):
        if Map[i][j] == 1:
            # zero_tmp = 0
            for d in range(4):
                dy = i + directy[d]
                dx = j + directx[d]

                if dy<0 or dx<0 or dy>101 or dx>101: continue
                if Map[dy][dx] == 0:
                    cnt += 1

            # if zero_tmp >= 1:
            #     cnt += 1

print(cnt)
