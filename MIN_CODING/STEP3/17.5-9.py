def masking(mask,target_list):

    for i in range(len(mask)):
        if mask[i] == 1:
            masked_list.append(target_list[i])
    
arr = list(map(int,input().split()))
mask = [1,0,1,0,1,0]
masked_list = []

masking(mask,arr)

min_v = 21e8
for element in masked_list:
    if element < min_v:
        min_v = element
        
print(f'arr[{arr.index(min_v)}]={min_v}')