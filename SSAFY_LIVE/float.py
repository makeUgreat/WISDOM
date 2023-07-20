'''
실수를 표현하는 자료형
프로그래밍 언어에서 float는 실수에 대한 근삿값(완전 정확한 값 아님)

@유한 정밀도
컴퓨터 메모리 용량이 한정되어 있어서.. 

'''

print(2 / 3)
print(5 / 3)

# 이러한 문제 때문에 실수 연산시 오류가 생길수도
# 예
a = 3.2 - 3.1
print(a)
b = 1.2 - 1.1
print(b)

# 1. 임의의 작은 수 활용
print(abs(a - b) <= 1e-10) 

# 2. math 모듈 활용
import math
print(math.isclose(a,b))

# e또는 E를 사용한 지수 표현
# 314 * 0.01 = 3.14
number = 314e-2
print(314*0.01)
print(number)
print(type(number))
print(314e2) 

# 소숫점 이하 첫번째 자리까지만,

print(round(0.5))  # 홀수는 5가 내림처리
print(round(1.5))  # 짝수는 원래대로 5가 올림처리 
print(round(2.5))  # 홀수는 5가 내림처리
print(round(3.5))
print(round(4.5))  # 홀수는 5가 내림처리
print(round(5.5))

# 소수점 이하 두번쨰 자리부터는 원래의 반올림 규칙을 따르는 걸 볼 수 있다.
print(round(0.15,1))
print(round(0.25,1))
print(round(0.35,1))
print(round(0.45,1))

# 이러한 이유는 파이썬이 부동소수점을 이용해서 실수를 표현하는 과정 중에
# 정확한 값이 아니라 근사값으로 계산을 함, 따라서 정확한 계산이 불가능하기 때문이다. 
# 그렇다면 반올림을 하라고 한다면 어떻게 처리할까?

# 1) 소수점에 0.5를 더한 뒤 내림처리 하는 방법

import math
print(math.floor(0.5+0.5))
print(math.floor(1.5+0.5))
print(math.floor(2.5+0.5))
print(math.floor(3.5+0.5))
print(math.floor(4.5+0.5))
print(math.floor(5.5+0.5))

# 2) 임의의 작은 수를 더한 뒤 반올림 처리

print(round(0.05 + 0.00001 ,1))
print(round(0.15 + 1e-4,1))
print(round(0.25 + 1e-3,1))
print(round(0.35 + 1e-2,1))
print(round(0.45,1))
print(round(0.55 + 1e-10,1))


'''
높이 - 하루 이동거리 = 소요일자 
if 높이 - 하루 이동거리 == 소요일자 :
    높이 - 하루이동거리
if 높이 - 하루 이동거리 < 하루 이동거리 
if 높이 - 하루 이동거리 > 하루 이동거리
'''