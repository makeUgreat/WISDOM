import sys
sys.stdin = open("BAEKJOON/for_min_input.txt", "r")

t = int(input())

for i in range(t):
    score = 0
    sum_score = 0
    test_case = input()
    for j in test_case:
        if j == 'O':
            score += 1
            sum_score += score 
        else:
            score = 0
            
    print(sum_score)
    
# score_list = []
# plus_score_list = []
# # for i in range(t):
#     test_case = input()
#     for j in range(len(test_case)):
#         if test_case[j] == 'O':
#             score_list.append(1)
#         elif test_case[j] == 'X':
#             score_list.append(0) 
            
#         print(f'{j}: {score_list}')
#         # plus_score_list.append(score_list)
#         # print(plus_score_list)
        
#         score_list.clear    
            
# for i in range(t):
#     test_case = input()
#     for j in range(len(test_case)):
#         if test_case[j] == 'O':
#             score_list.append(1)
#             while True: # test_case의 j번째가 O이면 그 다음칸도 O인지 확인하는 반복문
#                 if (j+k) <= len(test_case)-1:
#                     if test_case[j+k] == 'X': # 다음칸이 X면 score_list 의 합계를 plus에 넘기고 종료
#                         plus_score_list.append(sum(score_list))  
#                         break
#                     k += 1 # 다음 칸 이동해주는 변수에 1 추가 
#                     score_list.append(1)
#             score_list.clear
        
#             print(plus_score_list)
            


    