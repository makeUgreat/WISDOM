'''
dict
key-value 쌍으로 이루어진
'순서와 중복이 없는' '변경 가능한' 자료형
@시퀀스는 순서도 있고 중복도 있음 

key는 변경 불가능한 자료형만 사용 가능(str,int,float,tuple,range... // 리스트는 불가능)
value는 모든 자료형 사용 가능
중괄호로 표기

'''

my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {'apple': 12, 'list': [1,2,3]}

print(my_dict_1)
print(my_dict_2)
print(my_dict_3)
print(len(my_dict_3))

# dict는 key를 통해 value를 접근!!! 

print( my_dict_3['apple']) #인덱스 사용
print( my_dict_3['list'])

# 값을 바꿀 때에도 접근은 key로!!!
my_dict_3['apple'] = 1300
print(my_dict_3)


# 딕셔너리 메서드
# .clear() 

# .get(key[,default]), 키 연결된 값을 반환한거나 키가 없으면 None 혹은 기본값을 반환 

person = {'name': 'Alice', 'age': 25}
print(person.get('name'))
print(person['name']) # 얘는 없는 키 하면 KeyError 
print(person.get('country')) # 없어도 None (코드 계속 진행)
print(person.get('country','Unknown')) # 키가 없으면 기본값 반환 

# 반대는 .pop(key[,default])
# 단, pop은 없으면 KeyError.. 에러원하지 않으면 기본값 설정!

print(person.keys())  # 딕셔너리의 키만 출력 
for k in person.keys():
    print('for keys:', k)


print(person.values())
for value in person.values():
    print('for values:', value)

print(person.items())
for item in person.items():  # 튜플로 한 쌍식 출력
    print(item)            

for key, value in person.items(): # 언패킹을 통해 하나씩 출력 
    print(key, value) 

# .setdefault(key[,default])
# 키와 연결된 값을 반환
# @@@ 키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환 

person = {'name': 'Alice', 'age': 25}

print(person.setdefault('country','KOREA')) # -> 없는 키라면 새로운 키값쌍 추가
print(person.setdefault('weight',75)) # -> 없는 키라면 새로운 키값쌍 추가
print(person)

# .update([other]) 
# other가 제공하는 키/값 쌍으로 딕셔너리를 갱신
# 기존 키는 덮어씀

person = {'name': 'Alice', 'age':25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person) # 없는 키-값쌍은 만들고 있는 키-값 쌍은 덮어씀
print(person)   

person.update(age=50)
print(person) 




# -----------------------


# dictionary - 내부적으로 hash 라는 자료구조를 이용해서 만들어 놓은 자료형

st = {'kevin': 1, 'john': 2, 'bob': 3}

# 키와 벨류를 딕셔너리에 추가
st['Kate'] = 4
print(st)

# 키와 벨류를 딕셔너리에서 삭제
del st['Kate']
print(st)

# 딕셔너리에 key만 따로 빼오기
lst = st.keys()
print(lst)
print(list(lst)) # 활용하기 좋게 리스트형으로 변환 

# 딕셔너리에 value만 따로 빼오기
lst = st.values()
print(list(lst))


# 딕셔너리에 있는 key,vlaue 둘 다 빼오기
lst = st.items()
print(lst)           # 키값쌍은 튜플로 저장
print(list(lst))  

# 요소 하나씩 빼고싶을 땐 for문
for key, value in st.items():
    print(key, value)

for arg in st.items():
    print(*arg)            # * 을 이용해 변수 하나로도 언패킹 가능 



st = {'kevin': 1, 'john': 2, 'bob': 3}
# print(st['kevinna']) 딕셔너리에 없는 키라면 Error 

# 에러없이 출력하려면
print(st.get('kevinna'))       # 에러시 기본값 None, 따로 설정가능 

# 딕셔너리 삭제 (del, pop)
st = {'kevin': 1, 'john': 2, 'bob': 3}
st = st.pop('kevvvvvvvvvvvvvin', -1)  # pop은 없는 키 뽑으면 에러, 기본값 설정가능
print(st)