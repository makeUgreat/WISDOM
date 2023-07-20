'''
set
순서와 중복이 없는 변경 가능한 자료형 (dict와 특성 같음)
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