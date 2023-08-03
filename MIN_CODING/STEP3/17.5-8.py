def isExist(y,x):  # 0,0 / 0,1 

    for i in range(len(map_)):
        for j in range(len(map_[i])):

            if pix[y][x] == map_[i][j]:
                return 1
    return 0
            
            
# map 하드코딩
map_ = [
    [3,55,42],
    [-5,-9,-10]]

# pix 배열 
pix = []
for _ in range(2):
    line = list(map(int,input().split()))
    pix.append(line)



# pix의 값을 isExit 로 넘기고 
# isExist 함수에서 map에 그 값이 있는지 확인
for y in range(2): 
    for x in range(2):  
        result = isExist(y,x)  # -> 0,0 / 0,1 

        if result:
            print('Y',end=' ')
        else:
            print('N',end=' ')
    print()
