# Sequence Type, 
# 여러 개의 값들을 순서대로 나열하여 저장하는 자료
# str, list, tuple, range 
# 순서대로 나열 != 정렬

s = "HappysssSt"

print( s.find('S') ) # S의 첫 번째 위치를 반환. 없으면 -1을 반환
print( s.index('S') ) # S의 첫번째 위치를 반환. 없으면 Error (코드 중단)
print( s.isalpha() ) # 알파벳만으로 이루어져 있는지 확인, 공백,쉼표,문장부호 등 있으면 False 
print( s.isupper() ) # 문자열이 모두 대문자/ 소문자로 이루어져 있는지 확인 
print( s.islower() )
print( s.istitle() )


