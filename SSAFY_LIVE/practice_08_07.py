# lsts = [
#     [3,5,4],
#     [1,1,2],
#     [1,3,9]
# ]


# # 1,1 을 기준으로 상하좌우 값들의 합을 구하라
# # 델타배열 

# y,x = map(int,input().split())

# directy = [-1,1,0,0]
# directx = [0,0,-1,1]

# sum_ = 0 
# for i in range(4):
#     dx = x+directx[i]
#     dy = y+directy[i]
#     if dy<0 or dy>2 or dx<0 or dx>2:
#         continue
#     sum_ += lsts[dy][dx]

# print(sum_)
    
# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]

# #입력받은 좌표값의 대각선에 있는 값들의 곱 구하기

# y,x = map(int,input().split())

# directy = [-1,-1,1,1]
# directx = [-1,1,-1,1]

# multi = 1 
# for i in range(4):
#     dy = y + directy[i]
#     dx = x + directx[i]

#     if dy<0 or dy>4 or dx<0 or dx>4:
#         continue
#     multi *= arr[dy][dx]

# print(multi)

# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]


# y,x = map(int,input().split())

# directy = [-1,1,0,0]
# directx = [0,0,-1,1]

# sum_ = 0
# for i in range(len(directx)):
#     for j in range(1,4):
#         dy = y + directy[i]*j
#         dx = x + directx[i]*j
        
#         if dy<0 or dx<0 or dy>4 or dx>4:
#             continue
#         sum_ += arr[dy][dx]
# print(sum_)            


arr=[[1,2,3,4],
      [1,2,9,4],
      [1,9,3,9],
      [1,2,9,4]]


def isSum(y,x):
    directx = [-1,1,0,0]
    directy = [0,0,-1,1]
    sum_ = 0
    for i in range(len(directx)):
        dy = y + directy[i]
        dx = x + directx[i]
        if dx<0 or dy<0 or dy>3 or dx>3:
            continue
        sum_ += arr[dy][dx]
        
    return sum_

max_ = -21e8
max_i = 0
max_j = 0

for i in range(4):
    for j in range(4):
        if isSum(i,j) > max_:
            max_ = isSum(i,j)
            max_i = i
            max_j = j
    
print(max_,max_i,max_j)


        