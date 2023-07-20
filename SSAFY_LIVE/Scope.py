'''
Python의 범위, Scope
함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분

@scope
global scope: 코드, 어디에서든 참조할 수 있는 공간
local scope: 함수가 만든 scope (함수 내부에서만 참조 가능)

@variable
global variable: global scope에 정의된 변수
local variable: local scope에 정의된 변수

'''
def my_func():
    num = 1 # 함수 내부의 local scope에만 정의

# print(num) # global scope에는 참조 못함 

'''
variable lifecycle, 변수 수명주기
변수의 수명주기는 변수가 선언되는 위치와 스코프에 따라 결정됨
1. built-in scope
파이썬이 실행된 이후부터 영원히 유지
2. global scope
모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope
함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

'''

'''
Name Resolution, 이름 검색 규칙
파이썬에서 사용되는 이름(식별자)들은 특정한 namespace에 저장됨
아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라 부름
1. Local scope: 현재 작업중인 범위
2. Enclosed scope: local scope 보다 한 단계 위 범위
3. Global scope: 최상단에 위치
4. Built-in scope: 모든 것들 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)

@@ 함수 내에서는 바깥 scope의 변수에 '접근 가능'하나 '수정은 불가'

'''
num = 100 # global scope
def my_func():
    print(num) # local scope에는 num이 없으나 global scope까지 써칭하여 num찾음

my_func()


# 내장함수를 변수명으로 사용하면 안되는 이유
print(sum([1,2,3])) # 6

sum = 10
print(sum) # 10
#print(sum([1,2,3])) #'int' object is not callable
                    # 10([1,2,3]) 과 같은 의미 


# sum을 global scope의 변수로 선언함으로써
# built-in scope에 있는 내장함수 sum의 기능을 수행하지 못함 


a = 1
b = 2
def enclosed():
    a = 10
    c = 3
    
    def local(c):
        print(a, b, c)  # 10 2 500

    local(500)
    print(a, b, c) # 10 2 3

enclosed()
print(a,b) # 1 2


# global 키워드
# 변수의 스코프를 전역 범위를 지정하기 위해 사용
# 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용

num = 0 # 전역 변수
def increment():
    global num # num을 전역 변수로 선언
    num += 1

print(num) # 0
increment()
print(num) # 1