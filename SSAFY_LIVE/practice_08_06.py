# lst=[4,3,5,1,7,5,6,8,1,6,9,5]

# target = list(map(int,input().split()))
# n = int(input())


# def getSum(t):
#     sum_ = 0
#     for i in range(t,t+n):
#         sum_ += lst[i]
#     return sum_

# max_v = -21e8
# max_index = 0
# for tar in target:
#     if getSum(tar) > max_v:
#         max_v = getSum(tar)
#         max_index = tar
        
# print(max_index, max_v)


# 연속되는 숫자 3개의 합이 가장 클 때 의 값을 출력해 주세요
# lst= [[4, 5, 2, 6, 7, 3, 1],
#       [2, 9, 9, 6, 1, 6, 7]]

# def getSum(y,x):
#     sum_ = 0
#     for i in range(3):
#         sum_ += lst[y][x+i]
#     return sum_
        

# # 이동 for문 만들기
# max_v = -21e8
# for i in range(2):
#     for j in range(5):
        
#         if getSum(i,j) > max_v:
#             max_v = getSum(i,j)
# print(max_v)
            
# lst=[[1 ,2 ,3 ,4 ,5],
#      [2 ,4 ,2 ,1 ,3],
#      [3 ,4 ,5 ,2 ,5]]

# target=[3, 4, 5]

# def isPattern(y,x):
#     for i in range(3):
#         if target[i]!=lst[y][x+i]:
#             return 0
#     return 1

# for i in range(3):
#     for j in range(3):
#         ret=isPattern(i,j)
#         if ret:
#             print(i,j)
    
    
    

# lst=[[1 ,2 ,3 ,4 ,5],
#      [2 ,4 ,2 ,1 ,3],
#      [3 ,4 ,5 ,2 ,5]]

# target=[3, 4, 5]

# def isPattern(y,x):
    
#     for i in range(3):
#         if target[i] != lst[y][x+i]:
#             return 0
#     return 1
    
    
    
# for i in range(3):
#     for j in range(3):
#         if isPattern(i,j):
#             print(i,j)


lst=[[1 ,5 ,4 ,2],
    [1 ,3 ,4 ,2],
    [3 ,5 ,3 ,2],
    [2 ,6 ,4 ,1]]

def getSum(y,x):
    sum_ = 0
    
    for i in range(2):
        for j in range(3):
            sum_ += lst[i+y][j+x]
            
    return sum_

max_v = -21e8
for i in range(3):
    for j in range(2):
        if getSum(i,j) > max_v:
            max_v = getSum(i,j)

print(max_v)
