def KFC():
    target = int(input())
    for lst in lsts:
        if target in lst:
            return 1
        else:
            return 0

lsts = [
    [3,2,6,2,4],
    [1,4,2,6,5]
]

value = KFC()

if value == 1:
    print("값이 존재합니다")
elif value == 0:
    print("값이 없습니다")