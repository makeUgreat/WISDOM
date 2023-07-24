# 메써드 , 객체에 내장된 함수 


print('hello'.capitalize()) # 맨 앞글자 하나를 대문자로 



# .sort(reverse=True) 
# vs 
# .reverse()


lst = [1,3,2,8,1,9]
lst.sort(reverse=True) #원본 자체를 변경하기 때문에 어디에 할당하지 않음
print(lst) #내림차순으로 정렬

lst = [1,3,2,8,1,9]
lst.reverse()
print(lst) #정렬하지않고 역순으로 출력 


# sort 메서드 
# sorted 내장함수 

numbers = [1,3,2,5,6,4,5]
print( numbers.sort() ) # None -> 반환하지 않았다 -> 복사본을 만들지 않았다
print( sorted(numbers) ) # 정렬 후 반환하므로 print로 바로 출력가능, 원본이 바뀌지 않았다. 
 

numbers2 = [1,2,3]
# 1. 할당
list1 = numbers2

# 2. 슬라이싱
list2 = numbers2[:]

numbers2[0] = 100

print(list1)  # [100,2,3]
print(list2) # [1,2,3] 일듯?

# 슬라이스는 새로운 리스트를 만들어서 출력해서 원본을 수정해도 안달라짐 
# 할당하면 같은 주소값을 가리키므로 원본을 수정하면 출력도 달라짐


a1 = 'asdf'
# a1.sort() 문자열은 sort 메서드 안먹힘
print(a1)

a1 = sorted(a1)
print(a1)          # sorted 내장함수를 써서 솔팅가능
a1 = ''.join(a1)
print(a1) # join으로 한 문자열로 합침

# 문자열 정렬은 ord() 로 숫자로 바꾸고 정렬하는 방법도 있음 .

# .sort()는 반환하지 않지만 sorted()는 반환함
# 따라서 .sort()는 원본 자체를 바꾸지만
# sorted()는 원본을 두고 새로운 객체를 만들어 반환함 


# @@@@람다를 이용한 리스트 정렬 

lst = list(range(10))

ret = sorted(lst, key=lambda x:x) #오름차순 정렬 후 출력
print(ret)

ret = sorted(lst, key=lambda x:-x) #내림차순 정렬 후 출력 (문자열은 불가능, 아스키코드값에는 음수가 없기 때문)
ret = sorted(lst, key=lambda x:x, reverse=True) #내림차순 정렬 후 출력
print(ret)


lst = [(3,'banana'), (2,'apple'),(1,'carrot')]
ret = sorted(lst, key=lambda x:x[1], reverse=True)
print(ret)
ret = sorted(lst, key=lambda x:x[0], reverse=True)
print(ret)
