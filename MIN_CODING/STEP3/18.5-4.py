cnt = []

nums_1 = list(map(int,input().split()))
nums_2 = list(map(int,input().split()))

cnt = 0
for num_1, num_2 in zip(nums_1, nums_2):
    if num_1 == num_2:
        cnt += 1
        
print(f'{cnt}개')