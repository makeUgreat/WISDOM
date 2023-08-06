apart = [
    [15,18,17],
    [4,6,9],
    [10,1,3],
    [7,8,9],
    [15,2,6]
]
# level = 0

# def isPattern(family,apart):
#     global level
#     for i in range(5):
#         for mem in family:
#             if mem in apart[i]:
#                 level = i+1
#                 return 1
#     return 0


# family = list(map(int,input().split()))

# if isPattern(family,apart):
#     print(f'{level}층')
# gpt 코드 

def isPattern(family,apart):
    for floor, resident in enumerate(apart[::-1],start=1):
        if all(mem in resident for mem in family):
            return floor
    
family = list(map(int,input().split()))

result = isPattern(family,apart)
if result:
    print(f'{result}층')
