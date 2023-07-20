'''
lambda
간단한 연산이나 함수를 한 줄로 표현할 때 사용
함수를 매개변수로 전달하는 경우에도 유용하게 활용

'''

def addition(x,y):
    return x + y

result = addition(3,5)
print(result) # 8

# 이 함수를 lambda로 줄여서

addition = lambda x, y: x + y

result = addition(3, 5)
print(result)
print('-------------')

# map + lambda
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers)) #numbers iterable의 요소들을 각각 2씩 곱함
print(result)

# 한번 쓰고 버릴 이름 없는 함수 만들 때 유용
# 변수에 저장해서 쓸거면 function이 더 좋음 

def triple_number(x):
    return x * 3

result = list(map(triple_number, numbers))
print(result)

# 하지만 보통 이런 식으로 함수를 넣어주는게 더 명시적임 