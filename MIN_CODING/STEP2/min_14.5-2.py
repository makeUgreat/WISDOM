import sys
sys.stdin = open('MIN_CODING/input.txt','r')


# lsts = []
# t_case = int(input())
# for i in range(5):
#     line = list(map(int,input().split()))
#     lsts.append(line)


# if t_case == 1:
    
#     for i in range(len(lsts)):
#         for j in range(len(lsts[i])):            
#             if j > i:
#                 continue
#             print(lsts[i][j],end=' ')
#         print()
        
# elif t_case == 2:
#     index = 0
#     for i in range(len(lsts)):
#         for j in range(len(lsts[i])-index):
#             print(lsts[i][j],end=' ')
#         index += 1
#         print()


# gpt 코드
lsts = []
t_case = int(input())
for i in range(5):
    line = list(map(int, input().split()))
    lsts.append(line)

if t_case == 1:
    for i, row in enumerate(lsts):
        for j in range(i + 1):
            print(row[j], end=' ')
        print()

elif t_case == 2:
    for i, row in enumerate(lsts):
        for j in range(len(row) - i):
            print(row[j], end=' ')
        print()
