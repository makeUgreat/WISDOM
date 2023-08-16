arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

merge = []

i = 0
j = 0

while 1:
        
    if arr1[i] <= arr2[j]: # arr의 i번 인덱스가 arr2의 j보다 작으면
        merge.append(arr1[i]) # merge배열에 값을 추가하고
        i += 1 # i 포인터 1증가 
        if i == 4: 
            for k in range(j,4):
                merge.append(arr2[k])
            break
    
    if arr1[i] > arr2[j]: 
        merge.append(arr2[j])
        j += 1
        if j == 4:
            for k in range(i,4):
                merge.append(arr1[k])
            break

print(*merge)