'''
set
순서와 중복이 없는 변경 가능한 자료형 (dict와 특성 같음)
= 고유한 항목들의 정렬되지 않은 컬렉션 
non-sequence 

수학에서의 집합과 동일한 연산 처리 가능
중괄호로 표기 

'''
my_set_1 = set()    #set{}로 선언하면 dict임 
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

print(my_set_1) #set()
print(my_set_2) #{1, 2, 3}
print(my_set_3) #{1} 중복이 없으므로 1하나만 

#순서가 없으므로 set는 index도 없음!!!!!!!!!

my_set_1 = {1,2,3}
my_set_2 = {3,6,9}

#합집합
print(my_set_1 | my_set_2)  # 중복은 제거하고 표현
#차집합
print(my_set_1 - my_set_2) 
#교집합
print(my_set_1 & my_set_2) # 중복만 표현

# 메서드
# .add()
# .clear()

my_set = {1,2,3}
my_set.clear()
print(my_set) # {} 로 출력되지 않는 이유? -> {} 는 빈 딕셔너리이기 때문 

my_set = {2,3,5}
# .pop()
print( 'pop:', my_set.pop() )  # 랜덤 .. 이지만 세트는 해시테이블을 통한 주소로 값을 인덱스 하는데 
print( 'pop:', my_set.pop() )  
print( 'pop:', my_set.pop() )  
# 가장 처음의 주소의 값을 뽑아 옴, 다음 pop은 그 다음 주소의 값 
# 다만 정수는 연속적이기에 주소도 한번 배정하면 바꾸지않음 그래서 반복 출력해도 똑같은 값을 가져오는것
# 그러나 문자열은 매번 주소를 다르게 배정하기 때문에 출력때마다 달라짐
my_set = {'a','b','c'}
print( 'pop_str:', my_set.pop())
print( 'pop_str:', my_set.pop())

# 해쉬 값으로 확인햄해보면

print(hash(1))         # 정수는 매번 해쉬값 고정
print(hash(1))
print(hash('a'))        # 해쉬가 가변적임 
print(hash('a'))
# 그래서 pop을 "무작위"가 아니라 "임의"로 값을 뽑는다고옴
# "arbitrary" is not mean "random"





# print( 'pop(index):', my_set.pop(0))  set는 순서가 없어서 인덱스로 뽑기 불가능

# .remove(값) 없으면 ERROR 
# .discard(값) 없어도 에러없음
my_set.add(1)
print( my_set.discard(4) )
# 
