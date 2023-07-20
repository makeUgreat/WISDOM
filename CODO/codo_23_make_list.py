#1차원 리스트 생성
a = []

for i in range(10):
    a.append(0)
print(a)
print('---')

# 2차원 리스트 생성
a = []
for i in range(3):
    line = [] #안쪽 리스트로 사용할 빈 리스트 생성
    for i in range(2):
        line.append(0)
    a.append(line)

print(a)
print('---')

# 2차원 리스트 컴프리핸션 사용

a = [[0 for j in range(2)] for i in range(3)]
print(a)
print('---')

a = [[0] * 2 for i in range(3)]
# 0이 1개 들어있는 리스트[0]에 2를 곱하면 [0,0]이
# 되는 성질을 이용
print(a)
print('---')

# jagged list 만들기 
a = [3, 1, 3, 2, 5]
b = []

for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)
print(b)
print('---')

a = [[0]*i for i in [3,1,2,3,5]]
print(a)
print('---')

#2차원 리스트를 정렬할때는 sorted사용 