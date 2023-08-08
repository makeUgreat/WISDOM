arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]


lsts = [[0]*4 for _ in range(4)]

nums = list(map(int,input().split()))

put_num = 1
for num in nums:

    for i in range(4):
        for j in range(4):
            if arr[i][j] == num:
                lsts[i][j] = put_num
                put_num += 1
    

for lst in lsts:
    print(*lst)

    