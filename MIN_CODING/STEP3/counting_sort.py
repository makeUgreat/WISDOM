arr = [1,9,17,12,16,16,9]

DAT = [0] * (max(arr)+1)

for i in arr:
    DAT[ i ] += 1 

print(DAT)

# 위랑 같은 말 
# for i in range(len(arr)):
#     DAT[ arr[i] ] +=1

# 이제 DAT의 각 인덱스는 arr값을 뜻하고
# 각 인덱스의 값은 
# arr값의 갯수를 뜻함 

# DAT인덱스 = arr값
# DAT인덱스값 = arr값개수 

# DAT를 누적합으로 만들기(정렬을 위해)
for x in range(1,len(DAT)): # 처음 시작부분이 인덱스 초과나니까 1번 인덱스부터 시작
    DAT[x] = DAT[x] + DAT[x-1]
print(DAT)

# 누적합된 DAT를 배열에 넣기
sort_list = [0] * len(arr) # arr의 정렬 배열이니까 arr이랑 길이 같음


for k in range(len(sort_list)): # 정렬된 DAT의 값-1이 정렬할 배열의 인덱스번호
    
    DAT[ arr[k] ] = DAT[arr[k]] - 1  # k가 0이라면, arr[k] = 1이고 DAT[1]은
    index = DAT[ arr[k] ]
    sort_list[index] = arr[k] 

print(sort_list) 
    
