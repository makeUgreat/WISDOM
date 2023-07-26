'''
객체지향 프로그래밍
Object Oriented Programming

데이터와 해당 데이터를 조작하는 메서드를 하나의 객체로
묶어 관리하는 방식의 프로그래밍 패러다임


절차지향   함수(데이터)

-데이터와 해당 데이터를 처리하는 함수(절차)가 분리
-함수 호출의 흐름이 중요

객체 지향   데이터(객체).메서드

-데이터와 해당 데이터를 처리하는
메서드를(메시지)를 하나의 객체(클래스)로 묶음
-객체 간 상호작용과 메시지 전달이 중요
'''

# 클래스, Class 
# 파이썬에서 타입을 표현하는 방법 
# 객체를 생성하기 위한 설계도
# 데이터와 기능을 함께 묶는 방법을 제공

# 객체, Object
# 클래스에서 정의한 것을 토대로 메모리에 할당된 것
# '속성'과 '행동'으로 구성된 모든 것
# 클래스로 만든 객체를 인스턴스라고도 함
# 아이유는 객체다 (O)
# 아이유는 인스턴스다 (X)
# 아이유는 가수의 인스턴스다 (O)

'''
name = 'Alice'
print(type(name))    # <class 'str'>

-변수 name의 타입은 str클래스다.
-변수 name은 str클래스의 인스턴스이다.
===> 우리가 사용해왔던 데이터타입은 사실 모두 클래스였다.

'''


'''
객체(object)의 특징
타입(type): 어떤 연산자(operator)와 조작(method)이 가능한가??
속성(attribute): 어떤 상태(데이터)를 가지는가?
조작법(method): 어떤 행위(함수)를 할 수 있는가?


Object = Attribute + Method
'''
#클래스 정의
class person:
    pass

# 인스턴스 생성
iu = person()

# 메서드 호출
iu.메서드()

# 속성(변수) 접근
iu.attribute 
