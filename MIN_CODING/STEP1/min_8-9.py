lst = [[0 for _ in range(2)] for _ in range(3)]


def input_func():
    nums = list(map(int,input().split()))
    index = 0
    for i in range(3):
        for j in range(2):
            lst[i][j] = nums[index]
            index += 1
    return lst

def process_func(get_lst):
    sum = 0
    for i in get_lst:
        for j in i:
            sum += j
    
    return sum

def output_func(get_sum_lst):
    print(get_sum_lst)



result = input_func()
result2 = process_func(result)
output_func(result2)


