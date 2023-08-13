
def swap(a,b): 
    arr[a],arr[b] = arr[b],arr[a]
arr = list(map(int,input().split()))

pivot = arr[0]

left_index = 1
right_index = 7
tmp1 = 0
tmp2 = 0
tmp_b = 0
tmp_s = 0

while 1:
     
    if left_index == right_index:
        arr[0],arr[right_index-1] = arr[right_index-1],arr[0]
        break
    
    if arr[left_index] > pivot:
        tmp1 = 1
    else:
        left_index += 1
        
    if arr[right_index] < pivot:
        tmp2 = 1
    else:
        right_index -= 1
        
    if tmp1 and tmp2:
        arr[left_index],arr[right_index] = arr[right_index],arr[left_index]
        left_index += 1
        right_index -= 1

print(*arr)
        
    