def isExist(y,x,univer,get_lsts):
    if univer[y][x] in get_lsts: # univer 의 (y,x)값이 get_lsts 에 있으면
        return 1                # 1  반환 


lsts = [3,7,4,1,2,6]
univer = []

# univer 리스트에 2*2로 입력 값을 받는 코드
for _ in range(2):
    line = list(map(int,input().split()))
    univer.append(line)

get_lsts = set(lsts)

# 2차원 배열 univer의 각 요소를 isExist 함수로 넘겨서 판단하는 코드
for i in range(len(univer)):
    for j in range(len(univer[i])):
        if isExist(i,j,univer,get_lsts): # univer[i][j]의 값이 lsts에 있으면
            print('OK',end=' ')          # 행단위(j) 띄어쓰기 후 출력
        else:
            print('NO',end=' ')
    print()    
