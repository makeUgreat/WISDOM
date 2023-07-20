# 문자열 바꾸기 .replace()
str = "Hello, world!".replace("world", "Python")

print(str)

s = "Hello, world!"
s = s.replace("world!", "Python")
print(s)
print("----")

# 문자 바꾸기 .maketrans('바꿀문자','새문자')
#           .translate(테이블)

table = str.maketrans("aeiou", "12345")
s = "alphabet".translate(table)

print(s)
print("----")

# 문자열 분리하기 .split()
# 공백을 기준으로 분자열을 분리해 리스트로 만듦

print("apple pear grape pineapple orange".split())
print("apple, pear, grape, pineapple, orange".split(", "))
print("----")


# 구분자 문자열 및 문자열 리스트 연결하기 .join()
print(" ".join(["apple", "pear", "grape", "pineapple", "orange"]))
# 각 요소들을 ' '(공백)으로 묶었음
print("-".join(["apple", "pear", "grape", "pineapple", "orange"]))
# 각 요소들을 '-'(-)으로 묶었음
print("----")


# 대문자 변환 .upper()
print("python".upper())
# 소문자 변환 .lower()
print("PYTHON".lower())
print("----")


# 공백 삭제하기 왼 .lstrip() , 우 .rstrip() , 양쪽 .strip()
print("    python".lstrip())
print("python    ".rstrip())
print("   python   ".strip())
print("----")

# 특정 문자 삭제하기 왼 .lstrip('삭제할 문자')
#                   우 .rstrip('삭제할 문자')
#                   양 .strip('삭제할 문자')
print("!@ case ##!##".lstrip("!"))
print("!@ case ##!##".rstrip("#"))
print("!@ case ##!###".strip("##"))
# 각 방향에서 삭제할 문자를 찾고 다른 문자를 만나기 전까지 연속된 같은 문자 삭제
print("----")

# 문자열 정렬하기 왼.ljust(길이)
#                오.rjust(길이)
#                양.center(길이)
# 문자열을 지정된 길이로 만들고 문자를 채우고 남은 여백을 공백으로
print("Test".ljust(10), "end")
print("start", "Test".rjust(10))
print("start", "test".center(10), "end")
print("----")

# 메서드 체이닝, 메서드끼리 연결해서 호출하는 것
print("python".rjust(30).upper())
print("----")

# 문자열 '왼쪽'에 0 채우기 .zfill()
print("35".zfill(4))  # 4칸 만들고 문자 제외 남은 칸 0
print("35".zfill(10))  # 10칸 만들고 문자 제외 남은 칸 0
print("----")

# 문자열 위치찾기 왼 .find('찾을 문자열'), 우 .rfind('찾을 문자열')
print("apple pineapple".find('pl')) #처음 찾은 문자열의 인덱스 반환 'pl'이 시작하는 [2]
print("apple pineapple".find('app')) #처음 찾은 문자열의 인덱스 반환 'app'이 시작하는 [0]
print("apple pineapple".find('x')) #없으면 -1 반환
print("----")

# 비슷한 기능의 .index('찾을 문자열'), 단, 못 찾으면 -1이 아닌 error 반환
print("apple pineapple".index('pl'))
# print("apple pineapple".index('x')) # -1 아닌 에러 반환
print("apple pineapple".rindex('pl')) #마찬가지로 오른쪽 시작 있음
print("----")

# 문자열 개수 세기 .count('문자열')
print("apple pineapple".count('pl'))