# 이해하고 넘어가면 안됨!! 직접 타이핑 해보고 썻다 지웠다 하면서 익숙해지게


st = 'apple, banana, mango'

index = st.find('a')  # a의 첫 위치 0 반환
index = st.find('ㅋ')  # 없으면 -1 반환 

st.count('a') # 문자열에 a가 몇개인지 

# join 합치기
# 리스트 안 문자열 또는 문자를 하나의 문자열로 만들 때 주로 사용 
# 구분자.join 을 이용해서 합침 

st = ['a','p','p','l','e']
str2 = "".join(st)

print(str2)

st = ['apple', 'banana', 'mango']
str3 = ','.join(st)

print(str3)


# st = input().lower().split()  # 소문자로 입력받기 



# 공백 지우기
st = '   apple'
str2 = st.lstrip()

print(st)
print(str2)



# 문자열,튜플은 인덱스로 접근해서 값을 변경할 수 없음
# 문자열에서 문자를 변경하고 싶으면 replace 사용 

st = '  apple  ' 
str2 = st.replace('ap','mr') #.replace('바꿀문자','바뀔문자') 
print(str2)



# 리스트 관련 메소드

st = ['apple', 'banana', 'mango']
st.append('orange') # 리스트에 attribute 추가 
print(st)

# append는 항상 맨 뒤에 추가됨
# 중간에 넣고 싶으면 .insert 사용

st.insert(1,'kiwi')
print(st)

st = [1,2,3]
str2 = [4,5]
st.extend(str2)
print(st)

st.append(str2) 
print(st)

# append와 extend차이 잘 구분하기
# append는 새로운 리스트를 만들어 추가 

st.pop()
print(st)
st.pop(0)  #.pop() 은 index로 삭제, 빈칸일 경우 맨 마지막 인덱스 삭제
print(st)


# 인덱스가 아니고 값으로 지우고 싶으면 .remove()

st.remove(3)
print(st)

st = [ 1,1,1,3,3,4,5]
st.remove(3)
print(st)    # 만나는 가장 첫 값만 삭제 