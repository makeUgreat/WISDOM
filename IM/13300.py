import sys
sys.stdin = open('input.txt','r')

import math

N,K = map(int,input().split())
girl = []
boy = []

# 성별로 나누고 필요한 방 갯수 찾기
for _ in range(N):
    S,Y = map(int,input().split())

    if S == 0:
        girl.append(Y)
    else:
        boy.append(Y)

# 학년 별로 필요한 방 할당
years = [1,2,3,4,5,6]
girl_bucket = [0] * 7 #0~6
boy_bucket = [0] * 7 #0~

# 여학생 수 확인
for student in girl:
    girl_bucket[student] += 1

for student in boy:
    boy_bucket[student] += 1

need_room2 = 0

for i in range(1,len(girl_bucket)):
    need_room2 += math.ceil(girl_bucket[i]/K)
    need_room2 += math.ceil(boy_bucket[i]/K)

print(need_room2)
