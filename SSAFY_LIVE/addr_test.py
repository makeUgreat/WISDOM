# 불변 데이터의 경우 동적 주소할당 방식
# 특정 값이 특정한 주소에 할당되어 있고
# 변수가 특정 값을 참조하는 방식이라
# 참조하는 값이 같으면 두 변수의 주소도 같음 
a = 5
b = 3
print(id(a), id(b))
print(id(a) == id(b))  # 값이 달라서 주소도 다름
print('1번-----')

a = 3
print(id(a), id(b))
print(id(a) == id(b))  # a = 3, b = 3 값이 같으면 주소도 같음
print('2번-----')

a = 5
b = 3
a = b

print(id(a), id(b))
print(id(a) == id(b))  # 변수로 할당해도 값이 같아서 주소도 같음
print('2.5번-----')

# 가변 데이터의 경우 정적 주소할당 방식
# 리스트 별로 각기 다른 주소를 가지고 있다
# 따라서 변수(리스트)가 다른 변수(리스트)를 할당하면 그 변수(리스트)의 주소가 할당
# 주소를 참조하기 때문에 같은 값을 할당해도 서로 다른 주소를 가지고 있음

list = [1,2,3]
list_2 = [2,3,4] 
print(id(list), id(list_2))
print(id(list) == id(list_2)) 
print('3번-----')

list_2 = list
print(id(list), id(list_2))
print(id(list) == id(list_2)) # list_2가 list의 주소값을 참조하므로 둘은 같은 주소값을 가짐
print('4번-----')

list = [1]
list_2 = [1]
print(id(list), id(list_2))
print(id(list) == id(list_2)) # 두 리스트 모두 같은 값의 요소를 가지고 있더도 다른 주소값을 가지고 있어 다름 
print('5번-----')

list = list_2
list_2[0] = 300
print(list[0])    # list에 list_2의 주소값을 할당했으니 list_2의 값을 바꾸면 list의 값도 바뀜(list는 list_2의 리스트를 참조하므로)
print('6번-----')


# 생각해볼문제
lst = [[1,2],[3,4]] # 2차원 배열
lst2 = lst[:] # lst2 에 슬라이싱으로 lst 모든 요소 할당
lst[0][0] = 100 # lst의 0,0에 100 할당
print(lst2[0][0]) #lst2의 0,0 값은 과연 몇일까? 
print('7번-----')

# 1차원의 경우 안바뀜 
list = list_2[:]
print(id(list), id(list_2))
print(id(list) == id(list_2)) # 둘 주소값은 다름 
list_2[0] = 5555
print(list[0])    # 리스트가 아닌 슬라이스로 할당하면 슬라이스는 주소가 아닌 '값'을 복사하기 때문에  list_2[0]의 값을 바꿔도 list의 값은 바뀌지않음
print('8번-----')

# 2차원 리스트의 경우는 슬라이싱해도 바뀜
# 2차원 리스트 안의 1차원 리스트의 주소값은 여전히 달라지지만
# 안의 요소들을 가리키는 주소값들은 똑같아서 
# 2차원 배열에서 슬라이싱을 해도 요소값들은 바뀔 수 있음(똑같이 주소값 참조)


# 리스트의 경우 값은 같으나 다른 주소값을 가진 리스트를 할당하고 싶으면
# llst_2 = list.copy() 의 방법을 이용 
# list_2 = list 는 값 뿐만 아니라 주소도 같아서 list의 요소 변경시  list_2도 같이 변경



