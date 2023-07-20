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
