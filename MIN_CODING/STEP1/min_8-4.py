arr = list(map(int,input().split()))


i = len(arr) - 1 # 5
while i >= 0: # 6
    if arr[i] == 7:
        print(arr[i],end=' ')
        break
    print(arr[i],end=' ')
    i -= 1
