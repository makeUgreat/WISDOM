x = int(input())
nums = map(int,input().split())
count = 0

for num in nums:  # num의 약수들 중에 자기 자신만 있는 걸 찾으면 count 
    for j in range(2, num+1):
        if num % j == 0:   # j가 num의 약수이고
            if num == j:    # 그 약수들 중 에서도 자기 자신일 때  
                count += 1

            break

print(count)

# 영일 풀이 
# prime = []
# for i in range(1,101):
#     ar = []
#     for j in range(1,101):
#         if i%j == 0:
#             ar.append(j)
#         else:
#             pass
    
#     if len(ar) == 2:
#         prime.append(i)

# print(prime)

# def make_prime_nums():
#     prime_lst = list(range(1,1001))
#     for i in prime_lst:
#             if i % 2 == 0:
#                 prime_lst.remove(i)
#                 prime_lst.insert(i-1,0)
#             elif i % 3 == 0:
#                 prime_lst.remove(i)
#                 prime_lst.insert(i-1,0)
#             elif i % 5 == 0:
#                 prime_lst.remove(i)
#                 prime_lst.insert(i-1,0)
#             elif i % 7 == 0:
#                 prime_lst.remove(i)
#                 prime_lst.insert(i-1,0)

#     prime_lst.remove(1)
#     prime_lst.append(2)
#     prime_lst.append(3)
#     prime_lst.append(5)
#     prime_lst.append(7)

#     prime_lst = set(prime_lst)

#     return prime_lst



# num = int(input())
# nums = map(int,input().split())
# count = 0

# for j in nums:
#     if j in make_prime_nums():
#         count += 1


# print(count)