'''
recursive function, 재귀함수
함수 내부에서 자기 자신을 호출하는 함수
특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

@@ 예시 - 팩토리얼 
n!
n * (n-1)!
n * (n-1) * (n-2)!

f(4) = 4 * f(3)
f(3) = 3 * f(2)
f(2) = 2 * f(1)
f(1) = 1
'''
def factorial(n):
    if n == 0:  # 종료 조건 : n이 0이면 1을 반환
        return 1
    
    return n * factorial(n - 1) # 재귀 호출 : n과  n-1의 팩토리얼을 곱한 결과를 반환

# 팩토리얼 계산 예시
result = factorial(5)
print(result)
