arr = [
    [3,5,4,1],
    [1,1,2,3],
    [6,7,1,2]
]


tmp = list(map(int,input().split()))
nums = tmp
nums.append(tmp[0])

def trans(element,nums):
    
    for i in range(len(nums)):
        if nums[i] == element:
            return nums[i+1]
        
    return element 
    

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = trans(arr[i][j],nums)
       
for ar in arr: 
    print(*ar)
        
        