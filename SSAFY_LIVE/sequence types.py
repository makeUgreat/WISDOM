'''
여러 개의 값들을 순서대로 나열하여 저장하는 자료형
특징
1. 순서(Sequence) 
   값들이 순서대로 저장(정렬X)
2. 인덱싱 (Indexing)
   각 값에 고유한 인덱스(번호)를 가지고 있으며, 인덱스를 사용하여 특정 위치의 값을 선택하거나
   수정할 수 있음
3. 슬라이싱(Slicing)
   인덱스 범위를 조절해 부분적인 값을 추가할 수 있음
4. 길이(Length)
   len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음
5. 반복(Iteration)
   반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음

'''
# str 문자열
# 문자들의 순서가 있는 '변경 불가능한' 시퀀스 자료형 
print('Hello, World!')
print(type('Hello, World!'))

'''
Escape sequence
역슬래시 뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합
파이썬의 일반적인 문법 규칙을 잠시 탈출한다는 의미
 \n : 줄 바꿈
 \t : 탭
 \\ : 백슬래시
 \' : 작은따옴표
 \" : 큰따옴표

'''
print('철수야 \'안녕\'')
print('이 다음은 엔터\n입니다.')

'''
String Interpolation
문자열 내에 변수나 표현식을 삽입하는 방법
문자열에 f 또는 F 접두어를 붙이고 표현식을 {expression}으로 작성하여
문자열에 파이썬 표현식의 값을 삽입할 수 있음
'''
bugs = 'roaches'
counts = 13
area = 'living room'
print(f'Debugging {bugs} {counts} {area}')

#f f-string 응용 , f-string advanced
greeting = 'hi'
print(f'{greeting:>10}') #10칸 만들고 오른쪽 정렬
print(f'{greeting:^10}') #10칸 만들고 가운데 정렬
print(f'{greeting:<10}') #10칸 만들고 왼쪽 정렬
print(f'{3.141592:.4f}') # 소숫점 아래 4칸까지만 출력


# 문자열은 시퀀스 자료형이므로 시퀀스의 특징인 슬라이싱, 인덱싱 등 가능하며 길이가 있음
my_str ='hello'
# 인덱싱
print(my_str[1])  
# 슬라이싱
print(my_str[2:4]) 
# 길이
print(len(my_str))
 
'''
      h  e  l  l  o
index 0  1  2  3  4
index-5 -4 -3 -2 -1

'''

'''
슬라이싱, slicing
인덱스와 달리 마지막 값 -1 만큼만 가져옴
'''
print(my_str[:5]) # 처음 굳이 표현 안해도 가능
print(my_str[0:]) # 끝 굳이 표현 안해도 가능
print(my_str[0:5:2]) # 2칸단위로 가져오는 step
print(my_str[::-1]) # 문자열 뒤집어서 가져오기 

# my_str[1] = 'z' # 접근은 가능하지만 바꿀 수는 없음. 문자열은 불변 자료형 
                # 바꾸고 싶으면 새로운 문자열을 만들어서 수정해야함 


# 불변과 가변
my_str = 'hello'
#my_str[0] = 'z'

my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)

#리스트는 참조하고 있는 방향만 바꾸면 되니 기존 리스트에서 값을 바꿀 수 있지만
#문자열은 그럴 수 없으므로 새로운 문자열을 만들어야 수정가능(수정되는 것 처럼 보임)
#그래서 리스트를 참조를 모아놓은 객체라고도 말하기도함 

list_1 = [1, 2, 3]
list_2 = list_1  #list_2는 새로운 list_1을 만드는게 아니고 list_1의 주소를 추적하고 있으므로
#list_2는 동일한 list_1의 리스트(주소)를 참조

list_1[0] = 100

print(list_1) # [100, 2, 3]
print(list_2) # [100, 2, 3]

x = 10
y = x    # 불변 자료형의 경우 가변과 다르게 새로운 주소를 생성하고
         # 똑같은 주소를 참조하지 않으므로 y는 10(x의 값)이 할당.
         # 포인터의 개념인듯?

x = 20
print(x) 
print(y)
