import sys
sys.stdin = open("MIN_CODING/STEP3/input.txt","r")


arr_1 = list(map(int,input().split()))
arr_2 = list(map(int,input().split()))
result = []

i = 0
j = 0

while 1:
    if i >= 4 and j < 4:
        while j < 4:
            result.append(arr_2[j])
            j += 1
        break 

    if i < 4 and j >= 4:
        while i < 4:
            result.append(arr_1[i])
            i += 1
        break

    if arr_1[i] <= arr_2[j]:
        result.append(arr_1[i])
        i += 1
    
    elif arr_1[i] >= arr_2[j]:
        result.append(arr_2[j])
        j += 1

print(*result)