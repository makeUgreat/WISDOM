x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
    print(i, end=' ') # 딕셔너리를 반복문으로 돌리면 키만 가져옴, 값은 어디에?
print()

for i in x.items(): # items() 메서드로 튜플형 키-값 쌍을 가져오고
    print(i, end=' ')
print()

for i,j in x.items(): # 거기에 임시변수를 2개 지정하면 키, 값 출력
    print(i,j)

# 마찬가지로 .keys() 메서드를 사용하면 키만
# .values() 메서드를 사용하면 값만 

for i in x.keys():
    print(i, end=' ')
print()
for i in x.values():
    print(i, end=' ')
print()

# 딕셔너리도 컴프리헨션 가능
# 특정 '키' 를 삭제하는 pop메서드는 있으나(엄밀히 말하면 키,값쌍)
# 특정 '값' 을 삭제하는 메서드는 없음
# 딕녀서리의 특정 '값' 삭제해보기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# for key, value in x.items():
#     if value == 20:
#         x.pop(key)

# print(x)             
# for문 사용하면 에러 뜨면서 불가능

x = {key: value for key, value in x.items() if value != 20} # 딕셔너리 컴프리헨션 쓰면 특정 값 삭제 가능
# 값이 20이 아닌 key, value만 임시변수 key: value에 넣고 x 변수에 할당
print(x)
print()
# 중첩 딕셔너리
# 책의 제목과 책갈피한 페이지를 딕셔너리로 표현

library = {
    '수학의 정석': {
        '지은이': '오태식',
        '총 페이지': 500,
        '책갈피': 113
    },
    '국어의 기술': {
        '지은이': '이재황',
        '총 페이지': 700,
        '책갈피': 130
    },
    '과학의 신비': {
        '지은이': '김진명',
        '총 페이지': 1300,
        '책갈피': 555
    }
}

print(library)
print() 
print(library['과학의 신비'])
print()
print(library['과학의 신비']['총 페이지'])
print() 

# 이런식으로 찾을 수 있음. 중첩 딕셔너리는 json 파일에서 자주 사용

