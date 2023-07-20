'''
Functions
특정 작업을 수행하기 위한 '재사용 가능한' 코드 묶음

Built-in function, 내장 함수
파이썬이 기본적으로 제공하는 함수 (별도의 import없이 바로 사용 가능)

'''

# function call, 함수 호출
# 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드블록을 실행하는 것
#function_name(argument)

def make_sum(pram1, pram2):
    '''
    두 수를 받아 두 수의 합을 반환하는 함수
    >>> make_sum(1,2)
    3
    '''
    return pram1 + pram2 

'''
@함수 정의
함수 정의는 def 키워드로 시작
def 키워드 이후 함수 이름 작성
괄호안에 매개변수를 정의할 수 있음
매개변수(parameter)는 함수에 전달되는 값을 나타냄 

@함수 body 
콜론(:) 다음에 들여쓰기 된 코드 블록
함수가 실행 될 때 수행되는 코드를 정의
Docstring은 함수 body앞에 선택적으로 작성 가능한 함수 설명서

@함수 반환 값
함수는 필요한 경우 결과를 반환할 수 있음
return 키워드 이후에 반환할 값을 명시
return문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환

'''

# parameter, 매개변수, 함수를 정의할 때 함수가 받을 값을 나타내는 변수
# vs
# argument, 인자, 함수를 호출할 때 실제로 전달되는 값 

def add_numbers(x, y):   #x와 y는 매개변수(parameter)
    result = x + y
    return result 

a = 2
b = 3
sum_result = add_numbers(a, b)  #a와 b는 인자(argument)
print(sum_result)

# Positional Arguments, 위치인자
# 함수 호출 시 인자의 위치에 따라 전달되는 인자

def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Alice',25)   # !!위치인자는 함수 호출 시 반드시 값을 전달해야 함!!

# Default Argument Values, 기본 인자 값
# 함수 정의에서 parameter에 기본 값을 할당하는 것
# 함수 호출 시 인자를 전달하지 않으면, 기본값이 parameter에 할당됨

def greet(name, age=30):  # argument 미입력시 기본값 30 설정
    print(f'안녕하세요,{name}님! {age}살이시군요.')

greet('Bob')  # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie',40) # 안녕하세요, Charlie님! 40살이시군요.

# keyword Arguments, 키워드 인자
# 함수 호출 시, 인자의 이름과 함께 값을 전달하는 인자
# parameter와 arguments를 일치시키지 않고, 특정 parameter에 값을 할당할 수 있음
# 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
# !!단, 호출 시 키워드 인자는 인자 뒤에 위치해야함

def greet(name, age):  #그냥 위치 인자인가?
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Dave', age=35) # 호출할 떄 arguments에 값을 할당해서 호출
greet(age=35, name='Dave') # 순서를 지키지 않아도 되는 것이 위치인자와 차이
# greet(age=35, 'Dave') # positional argument follows keyword argument

# Arbitrary Argument Lists, 임의의 인자 목록
# 정해지지 않은 개수의 인자를 처리하는 인자
# 함수 정의 시 parameter 앞에 *를 붙여 사용하며, 여러개의 인자를 tuple로 처리
total = 0 
def cal_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계: {total}') 

print( cal_sum(1,2,3) ) # function에 return 이 없어서 None 반환
print( cal_sum(1,2,3,45,321) ) # function에 return 이 없어서 None 반환

# Arbitrary Keyword Argument Lists, 임의의 키워드 인자 목록
# 정해지지 않은 개수의 '키워드 인자'를 처리하는 인자
# 함수 정의 시 parameter 앞에 **를 붙여 사용하며, 여러개의 인자를 dict으로 처리
def print_info(**kwargs):
    print(kwargs)

print_info(name='Eve', age=30, weight=83)
# 정해지지 않은 키워드를 사용자가 임의로 정해서 넣음 

'''
함수 인자 권장 작성순서
위치 -> 기본 -> 가변 -> 키워드 -> 가변 키워드
호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함
@절대적인건 아님 상황에따라 유연하게 
'''
#def func(pos1, pos2, default_Arg='default', *args, kwd, **kwd_args)

