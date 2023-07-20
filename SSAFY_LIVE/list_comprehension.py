# 리스트를 생성하는 일반적인 방법
new_list = []
for i in range(10):
    if i % 2 == 1:
        new_list.append(i)
print(new_list)

# 컴프리핸션을 이용한 리스트 생성 
new_list2 = [i for i in range(10) if i % 2 == 1]
print(new_list2)

new_list2 = list(i for i in range(10) if i % 2 == 1)
print(new_list2)

'''
리스트 컴프리핸션이 편하기는 하지만
!!!가독성!!!은 떨어짐

따라서 첫번째 방법이 더 좋은 코드임
그렇다고 리스트 컴프리핸션을 몰라서는 안됨
저 둘을 자유롭게 변환할 수 있어야함!

'''


# 인덱스와 값을 같이 출력해주는 enumerate 

fruits = ['apple', 'banana', 'cherry']
print(enumerate(fruits)) # 인덱스와 값을 같이 저장(주소에 저장중)  
print(list(enumerate(fruits))) # 리스트로 표현하면 튜플로 묶여있는 걸 볼 수  있음

for index, fruit in enumerate(fruits): # 튜플 값을 요소 2개로 언팩킹하면 값이 출력!
    print(f'인덱스 {index}: {fruit}')


