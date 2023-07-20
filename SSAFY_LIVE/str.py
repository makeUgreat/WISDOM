# (높이 / 이동거리)
#  
# (높이 / 이동거리) + 1 소요일  
# .. 올림처리? 

# "순서" 개념이 있는 자료형 -> 문자열 list tuple range
print('오늘은 컨디션이 "100%" 입니다.')
# "순서"의 개념이 무색한 자료형 -> set dictionary

s="abcdefg"
print(s[:3]) #ab -> abc
print(s[3:]) #cdefg -> defg
print(s[2:5]) #cd -> cde
print(s[5:2:-1]) #fedc -> fed
print(s[2:5:2]) #ce 
print(s[::-1]) #gfedcba
print(s[-2]) #f