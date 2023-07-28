lsts = [
    ['A','B','C','D','E','F','G'],
    [4,2,5,1,6,7,3]
]

start_index = 0
destination_index = 0
distance = 0

ch1, ch2 = input().split()
for i in range(len(lsts[0])):
    if lsts[0][i] == ch1:
        start_index = i
    
    if lsts[0][i] == ch2:
        destination_index = i

if start_index < destination_index:
    for j in range(start_index+1,destination_index):
        distance += lsts[1][j]  
elif start_index > destination_index:
    for j in range(destination_index+1,start_index):
        distance += lsts[1][j]  

print(distance)


#gpt 

# 입력과 리스트 초기화
lsts = [
    ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    [4, 2, 5, 1, 6, 7, 3]
]

# 사용자로부터 민스가 있는 나라와 지효가 있는 나라를 입력 받습니다.
ch1, ch2 = input().split()

# 시작 인덱스와 도착 인덱스를 바로 구합니다.
start_index = lsts[0].index(ch1)
destination_index = lsts[0].index(ch2)

# 시작 인덱스가 도착 인덱스보다 작을 때
if start_index < destination_index:
    # 시작 인덱스 다음부터 도착 인덱스 전까지의 거리를 더합니다.
    distance = 0
    for i in range(start_index + 1, destination_index):
        distance += lsts[1][i]
# 시작 인덱스가 도착 인덱스보다 클 때
elif start_index > destination_index:
    # 도착 인덱스 다음부터 시작 인덱스 전까지의 거리를 더합니다.
    distance = 0
    for i in range(destination_index + 1, start_index):
        distance += lsts[1][i]
# 시작 인덱스와 도착 인덱스가 같을 때
else:
    distance = 0

# 출력
print(distance)
