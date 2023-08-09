arr = list(map(int,input().split()))

for j in range(4):
    for i in range(4+j):
        print(arr[i],end=' ')
    print()