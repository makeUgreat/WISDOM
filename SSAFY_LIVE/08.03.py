# # # delta 배열 = 방향배열 = direct 배열
# # # 코테 사용률 90%!
# #
# # # flood fill?
# #
# # # lsts = [
# # #     [3,5,4],
# # #     [1,1,2],
# # #     [1,3,9]
# # # ]
# # #
# # # y,x = map(int,input().split())
# # #
# # # directy=[-1,1,0,0]
# # # directx=[0,0,-1,1]
# # # #       상 하 좌 우
# # # sum_ = 0
# # # for i in range(4):
# # #     dy = y+directy[i]
# # #     dx = x+directx[i]
# # #     # 배열의 범위를 벗어날 경우:
# # #     if dy<0 or dy>2 or dx<0 or dx>2: continue
# # #     sum_ += lsts[dy][dx]
# # #
# # # print(sum_)
# #
# #
# #
# # #입력받은 좌표값의 대각선에 있는 값들의 곱 구하기
# #
# # arr = [ [3, 5, 4, 5, 6],
# #         [1, 1, 2, 7, 8],
# #         [1, 2, 9, 1, 2],
# #         [3, 5, 4, 5, 6],
# #         [1, 1, 2, 7, 8]]
# #
# # y,x = map(int,input().split())
# # #
# # # directy = [-1,1,-1,1]
# # # directx = [-1,-1,1,1]
# # #
# # # multi = 1
# # # for i in range(4):
# # #     dy = y + directy[i]
# # #     dx = x + directy[i]
# # #     if dx < 0 or dx > 4 or dy < 0 or dy > 4: continue
# # #     multi *= arr[dy][dx]
# # # print(multi)
# #
# # directy = [-1,1,0,0]
# # directx = [0,0,-1,1]
# #
# # sum_ = 0
# # for i in range(len(directx)):
# #     for j in range(1,4):
# #         dy = y + directy[i]*j
# #         dx = x + directx[i]*j
# #
# #         if dx <0 or dx > 4 or dy < 0 or dy > 4:
# #             continue
# #         sum_ += arr[dy][dx]
# # print(sum_)
# #
# arr=[
#     [1,2,3,4],
#     [1,2,9,4],
#     [1,9,3,9],
#     [1,2,9,4]
# ]
# # 위 아래 좌 우 좌표들의 합이 가장 큰 곳의 합과 그때의 좌표값 출력하기
#
# def isSum(y,x):
#     directy = [0,0,-1,1]
#     directx = [-1,1,0,0]
#     sum_ = 0
#     for i in range(4):
#         dy = y + directy[i]
#         dx = x + directx[i]
#         if dy<0 or dx<0 or dy>3 or dx>3: continue
#         sum_ += arr[dy][dx]
#     return sum_
#
# Max = -21e8
# Max_i = 0
# Max_j = 0
#
# #
# # sum_ = 0
# # directy = [-1,1,0,0]
# # directx = [0,0,-1,1]
# # max_v = -21e8
# #
# # y,x = map(int,input().split())
# #
# # for i in range(len(directy)):
# #     dy = y + directy[i]
# #     dx = x + directx[i]
# #
# #     if dy < 0 or dx <0 or dy > 2 or dx > 4: continue
# #     sum_ += arr[dy][dx]
# #
# #     if sum_ > max_v:
# # #         max_v = sum_
# #         max_dx = dx
# #         max_dy = dy
# #
# # print(max_v,max_dx,max_dy)
#
#
#


arr = [[3, 5, 4, 5],
       [1, 1, 2, 7],
       [1, 2, 9, 1],
       [3, 5, 4, 5]]

# 4*4 배열안의 값의 합을 구할 것입니다.
# for문으로 구한 후 출력해 주세요.

# sum1= 1+1+2+3+4+5 를 하면 출력은 16이 출력이 될 것이고
# sum2= 5+4+5+2+7+1 를 하면 출력은 24가 출력이 될 것입니다.
# sum1 = 0
# for i in range(len(arr)):
#     for j in range(0,i):
#         if i != j:
#             if j < 4:
#                 sum1 += arr[i][j]
#
# print(sum1)
#
# sum2 = 0
# for i in range(len(arr)):
#     for j in range(4-i,0,-1):
#         if i != j:
#             sum2 += arr[i][j]
# print(sum2)
#
# sum3 =0
# sum4 = 0
# for i in range(4):
#     for j in range(4):
#         if i == j:
#             sum3 += arr[i][j]
#         if i+j == 3:
#             sum4 += arr[i][j]
#
# print(sum3)
# print(sum4)


arr = [[3, 5, 4, 5],
       [1, 1, 2, 7],
       [1, 2, 9, 1],
       [3, 5, 4, 5]]

lsts =[]
sum_ = 0
for i in range(4):
    for j in range(4):
        if i-j == i or i-j == j or i-j == 0:
            sum_ += arr[i][j]
    lsts.append(sum_)
    sum_ = 0


print(lsts)