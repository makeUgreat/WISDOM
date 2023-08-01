arr_1 = list(map(int,input().split()))
arr_2 = list(map(int,input().split()))
result = []
for i in range(1,5):
    result.append(arr_1[i-1] + arr_2[-i])

print(*result)