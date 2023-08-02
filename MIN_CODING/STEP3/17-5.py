def isExist(num,lsts):
    for lst in lsts:
        if num in lst:
            return 1
    return 0

lsts = [
    [3,5,9],
    [4,2,1],
    [5,1,5]
]

nums = map(int,input().split())
for num in nums:
    if isExist(num,lsts):
        print(f'{num}:존재')
    else:
        print(f'{num}:미발견')
