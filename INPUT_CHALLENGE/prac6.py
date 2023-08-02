a = [8, 3, 5, 2, 5, 7, 2, 4]


n = int(input())
b = list(map(int,input().split()))

# 버켓을 등록
bucket = [0] * 9 # 데이터가 8개니까 인덱스슬 위해 1개 더 큰 9개 등록

for i in range(len(a)):
    bucket[a[i]] += 1   # 데이터 값이 -> 버켓의 인덱스 
    
for i in range(len(b)):
    print(f'{b[i]}:{bucket[b[i]]}개 있음')

# 입력 받은 값(b리스트,찾고 싶은 값)은 버켓의 인덱스이자
# 동시에 그 인덱스는 입력받은 값의 갯수