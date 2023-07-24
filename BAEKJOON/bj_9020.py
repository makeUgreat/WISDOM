import sys
sys.stdin = open("BAEKJOON/input.txt", "r")


cases = int(input())
prime_num_lst = []
result_value = []

for i in range(cases): 
    nums = int(input())

    for num in range(1,nums+1):    # num 사이에 있는 소수들 뽑기
        for j in range(2,num+1):
            if num % j == 0:
                if num == j:
                    prime_num_lst.append(num)
                break

    for k in range( len(prime_num_lst) ):   # 2, 3, 5 ,7
        result_value.clear()
        if prime_num_lst[k] + prime_num_lst[k] == nums:
                result_value.append(prime_num_lst[k])
                result_value.append(prime_num_lst[k])
        else:
            for l in range( len(prime_num_lst) ):
                    if k+l < len(prime_num_lst):
                        if prime_num_lst[k] + prime_num_lst[k+l] == nums:
                            result_value.append(prime_num_lst[k])
                            result_value.append(prime_num_lst[k+l])
        print(nums, result_value)
    prime_num_lst.clear()                         
