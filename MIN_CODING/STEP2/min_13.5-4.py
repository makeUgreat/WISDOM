lsts= [
    [3,4,1,6],
    [3,5,3,6],
    [5,4,6,0]
]

# 세번째 Line 추가 
line = list(map(int,input().split()))
lsts.insert(2, line)

max_list = []
min_list = []
for lst in lsts:
    max_list.append(max(lst))
    min_list.append(min(lst))

max_value = max(max_list)
min_value = min(min_list)


# 최대,최솟값 좌표 찾기,인덱스
flag1 = True

for i in range(len(lsts)):
    if flag1:
        for j in range(len(lsts[i])):
            if lsts[i][j] == max_value:
                print(f'MAX={max_value}({i},{j})')
                flag1 = False
flag1 = True 
for i in range(len(lsts)):
    if flag1:
        for j in range(len(lsts[i])):
            if lsts[i][j] == min_value:
                print(f'MIN={min_value}({i},{j})')
                flag1 = False