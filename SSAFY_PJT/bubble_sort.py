arr = [4,7,1,3,5]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
print(arr)

