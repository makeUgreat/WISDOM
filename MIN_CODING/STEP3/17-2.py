def offset_func(index, target, arr):
    for i in range(len(arr)):
        if arr[i] == target:
            offset = i - index
            return offset

arr = [5,9,4,6,1,5,8,9]
index, target = map(int,input().split())

print(offset_func(index,target,arr))


