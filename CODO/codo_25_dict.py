x = {'a':10, 'b':20, 'c':30, 'd':40}
x.setdefault('e')  #딕셔너리에 키 e추가
x.update(e=50) #키 e에 값 50 추가
print(x)

x.update(a=100, d= 400)
x.update(h=100) # 없는 키,값 쌍도 추가 가능
#!!!단 키가 문자열일 때만 가능!!!
print(x)

y = {1: 'one', 2: 'two'}
# y.update(4='four')  , 불가능
y.update({1: 'one', 3: 'three'})
print(y)

y.update([ [2, 'TWO'], [4, 'FOUR'] ]) #리스트나 튜플 형식으로도 추가 가능
print(y)

y.update(zip([5,6,7,8], ['five','six','seven','eight']) ) # zip을 이용하면 
#한번에 여러 키:값 수정 가능 (키가 숫자여도 추가 가능)
print(y)
#setdefault 는 키-값 추가만 가능
#update는 추가 및 수정도 가능

x.pop('a')  # 딕셔너리에서 키-값 쌍 삭제
print(x)

print( x.pop('g',1) ) # pop(키,기본값) 없는 키를 제거하면 기본값 반환

# .popitem() 마지막 키-값 쌍 삭제후 튜플로 반환
print( x.popitem() ) 

# .clear() 모든 키-값 쌍 삭제

# .get(키) , 딕셔너리에서 특정 키의 값을 가져옴
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.get('a'))
print(x['a']) # get과 기능같음

print(x.get('z',1010)) # pop과 마찬가지로 기본키를 지정해
                       # 없는 키를 호출하면 기본키 반환

# .items() 딕셔너리의 키-값쌍 모두 가져옴 
print(x.items())
# .keys() 키를 모두 가져옴
print(x.keys())
# .values() 값을 모두 가져옴
print(x.values())

# 이 외 dict 메써드 많으니 코딩도장 정독 