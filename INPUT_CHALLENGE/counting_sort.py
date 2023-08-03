arr = [4, 7, 1, 4, 2, 4, 3]

# 버켓 등록
bucket = [0] * len(arr)
for i in range(len(arr)):
    bucket[arr[i]] += 1  # arr의 값 -> bucket의 인덱스 -> 카운트+1

for i in range(len(bucket)):