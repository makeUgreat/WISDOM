#문자열 안에서 특정 부분만 원하는 값으로 바꿀 때
#서식 지정자 또는 문자열 포매팅 사용

print('I am %s' % 'kjm') # %s 포맷자리에 % 뒤 문자열 넣음 
name = 'IHB'
print('My G.F  name is %s' % name)
print('----')

print('My height is %d' % 186,'cm')

#실수, float
print("This swimming pool's depth is %f" % 3,"m" )
print("This swimming pool's depth is %.1f" % 3,"m" ) #소숫점 제한하고 싶으면 포맷에 숫자


# 서식 지정자로 문자열 정렬하기 .just()+포멧형?
print("start %10s" % '12345') # 앞 start문자와 별개로 10칸을 만든뒤 % 뒤의 문자열을 채우고 남은 것 만큼 공백채움
print("start %-10s" % "12345") # 왼쪽부터 채울 땐 -

# 서식 지정자 여러개 넣기

print("Today is %d %s." % (17, "July")) # 꼭 괄호로 묶어야함 
print('----')


# format 메서드 사용 
print("Hello, {0}".format('world!'))
print("Hello, {0} {2} {1}".format('Python','Script',3.6)) # 숫자 인덱스대로
print("Hello, {} {} {}".format('Python','Script',3.6)) # 생략하면 순서대로

# 문자열 포매팅에 변수를 그대로 사용
language = 'Python'
version = 3.6

print(f'Hello, {language} {version}')

# 금액 천 단위로 콤마 넣기 format(숫자, ',')
print( format(1493500, ',') )