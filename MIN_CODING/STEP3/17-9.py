def isCount(get_num,get_vect):
    cnt = 0
    for i in range(len(vect)):
        for j in range(len(vect[i])):
            if get_num == get_vect[i][j]:
                cnt += 1

    return cnt 


vect = [
    [3,7,4],
    [2,2,4],
    [2,2,5]
]

target = list(map(int,input().split()))
max_value = 0
max_num = 0

for num in target:
    if isCount(num,vect) > max_value:
        max_value = isCount(num,vect)
        max_num = num

print(max_num)
