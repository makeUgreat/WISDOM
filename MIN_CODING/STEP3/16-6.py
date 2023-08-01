arr = list(map(int,input().split()))

for i in range(len(arr)-1):
    tmp = arr[i] + arr[i+1] 
    arr[i+1] = tmp

print(*arr)
