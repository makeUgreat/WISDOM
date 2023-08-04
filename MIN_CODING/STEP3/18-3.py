lsts = [
    [1,3,3,5,1],
    [3,6,2,4,2],
    [1,9,2,6,5]
]


# n = int(input())

tmp = []
# lsts 를 1차원 배열로 바꾸고
for lst in lsts:
    tmp.extend(lst)

# lsts의 수를 계산하는 배열 생성
bucket = {} # n이 1~9 사이의 정수이므로
for t in tmp:
    bucket[t] = bucket.get(t,0) + 1

# 숫자를 입력받고
n = int(input())

# 배열에 입력받은 숫자 개수만큼 존재하는 값 출력 
sort_list = []
for key,value in bucket.items():
    if value == n:
        sort_list.append(key) # 정렬을 위해 값이 n인 key를 sort_list에 추가

sort_list.sort()
print(*sort_list)