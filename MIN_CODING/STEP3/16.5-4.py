index_1, index_2 = map(int,input().split())

arr = [0] * 6
arr[0] = index_1
arr[1] = index_2

for i in range(0,4):
    tmp = arr[i] * arr[i+1]
    arr[i+2] = tmp

print(arr[5])