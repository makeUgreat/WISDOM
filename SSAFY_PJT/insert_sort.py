arr = [4,7,1,3,5]
result = []
for i in range(5):
    result.append(arr[i])
    for j in range(i,0,-1):
        if result[j-1] > result[j]:
            tmp = result[j]
            result[j] = result[j-1]
            result[j-1] = tmp
        else:
            break

print(result)
