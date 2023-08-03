def checkKalcs(get_kalcs,get_row):

    cnt = 0
    for kalc in get_kalcs:
        if get_row[0] <= kalc <= get_row[1]:
            cnt += 1
        
    return cnt
    

levelTable = [
    [10,20],
    [30,60],
    [100,150],
    [200,300]
]

kalcs = list(map(int,input().split()))

for i in range(len(levelTable)):
    print(f'lev{i}:{checkKalcs(kalcs,levelTable[i])}')
