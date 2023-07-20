'''
list
여러 개의 값을 순서대로 저장하는 '변경 가능한' 시퀀스 자료형

0개 이상의 객체를 포함하며 데이터 목록을 저장 (빈 리스트 만들 수 있음)
대괄호로 표기
데이터는 어떤 자료형도 저장할 수 있음(문자열,정수,실수,리스트,딕셔너리,튜플 등등)

'''

my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
print(len(my_list))
print(my_list[4][-1])
print(my_list[-1][1][0])

#문자열은 불변 리스트는 가변
my_list[0] = 100
print(my_list)


'''
tuple
여러 개의 값을 순서대로 저장하는 '변경 불가능한' 시퀀스 자료형

0개 이상의 객체를 포함하며 데이터 목록을 저장
소괄호로 표기
데이터는 어떤 자료형도 저장할 수 있음(문자열,정수,실수,리스트,딕셔너리,튜플 등)

튜플의 불변 특성을 사용해 안전하게 여러 개의 값을 전달, 그룹화, 다중 할당 등
개발자가 직접 사용하기 보다는 '파이썬 내부 동작'에서 주로 사용됨
리스트 대비 접근속도 빠름 

'''
my_tuple_1 = ()
my_tuple_2 = (1,) # 튜플의 요소가 1개일 때 ,를 넣어주는 이유는 사칙연산의 소괄호와 구분하기 위해
my_tuple_3 = (1, 'a', 3, [1,2], (3,4))

print(my_tuple_1)
print(my_tuple_2)
print(my_tuple_3)

x, y = (10, 20)
x, y = 10, 20   # 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호는 생략 가능
print(x)
print(y)

'''
range
연속된 '정수' 시퀀스를 생성하는 '변경 불가능한' 자료형

range(n)
0부터 n-1까지의 숫자 시퀀스

range(n, m)
n부터 m-1까지의 숫자 시퀀스 

'''
range_1 = range(5)
range_2 = range(1,10)

print(range_1)
print(range_2)
print(list(range_1)) # range의 요소를 뽑고 싶을 때는 시퀀스 자료형으로 
print(tuple(range_2))



