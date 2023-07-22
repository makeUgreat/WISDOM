def num_count(get_nums):
    
    for k in range(0,10):
        count = 0
        for num in get_nums:
            if num == k:
                count += 1
        
        print(count)

A = int(input())
B = int(input())
C = int(input())
result = A*B*C
list_result = []
for i in str(result):
    list_result.append(i)
    

num_count(list(map(int,list_result)))