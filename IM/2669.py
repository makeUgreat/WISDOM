import sys
sys.stdin = open('IM/input.txt','r')

Map = [[0] * 100 for _ in range(100)]


for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    
    for i in range(y1,y2):
        for j in range(x1,x2):
            Map[i][j] = 1
    # print()
    # print(f'x1:{x1},y1:{y1},x2:{x2},y2:{y2}')
    # for m in Map:
    #     print(*m)

cnt = 0
for i in range(100):
    for j in range(100):
        if Map[i][j] == 1:
            cnt+=1


print(cnt)