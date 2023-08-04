map = [
    [65000, 35, 42, 70],
    [70, 35, 65000, 1300],
    [65000, 30000, 38, 42]
]

bucket = [0] * (65000 + 1)


for i in range(len(map)):
    for j in range(len(map[i])):
        bucket[ map[i][j] ] += 1


print(bucket.index(max(bucket)))

'''
map = [
    [65000, 35, 42, 70],
    [70, 35, 65000, 1300],
    [65000, 30000, 38, 42]
]

# 딕셔너리를 사용하여 숫자들의 발생 빈도를 계산
number_frequency = {}

for row in map:
    for num in row:
        if num in number_frequency:
            number_frequency[num] += 1
        else:
            number_frequency[num] = 1

# 가장 많이 발생한 숫자 찾기
most_common_number = max(number_frequency, key=number_frequency.get)
print(most_common_number)

'''