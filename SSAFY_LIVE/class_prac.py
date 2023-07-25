# 라이브 내용은 없지만
# 알면 도움이 될 만한 클래스 하나 소개 시켜 드리도록 하겠습니다.
# counter라는 클래스 사용법

from collections import Counter 
lst = ['apple', 'mango', 'banana', 'mango', 'apple', 'banana', 'mango']

# counter 클래스는 중복된 데이타가 각각 몇개씩 있는지 알려주는 클래스
print(Counter(lst))

ret = dict(Counter(lst))
print(ret)

# 문자열 중에서 가장 많이 사용된 알파벳이 무엇인지 알고 싶을때도 사용가능
st = 'an applemango'
print(Counter(st))
ret = dict(Counter(st))
print(ret)

# 가장 많이 사용된 알파벳을 출력하시오~
# sort 연습 후 가장 많이 사용된 알파벳 출력

ret = sorted(ret.items(), key=lambda x:x[1], reverse=True)
# items 를 사용하면 key와 tuple로 반환하는데
# x[1] -> 즉, 알파벳 별로 사용된 갯수를 기준으로 sort함
# reverse=True 를 통해서 내림차순으로 정렬 

print(ret[0][0]) # -> 가장 많이 존재하는 알파벳 출력해보기! 



# 알면 좋은 방법 (가장 많이 사용된 문자 출력하기 예시)  -> counter 라는 클래스 안에
# most common 이라는 메서드가 있어서 그것을 이용하는 예시를 보겠다
st = 'an applemango'
ret = Counter(st).most_common(1)
print(ret)
print(ret[0][0])

# 추가적으로 counter 클래스를 사용하면 문자열의 덧셈과 뺄셈도 가능
# 예를 한번 들어보도록 하겠습니다 

a = Counter('apple')
b = Counter('mango')
print(a+b) # a문자열에서 사용된 알파벳 개수 + b문자열에서 사용된 알파벳 개수
print(a-b) # a문자열에서 b문자열에서 사용된 알파벳을 뺀 후, 사용된 알파벳 개수도 확인가능


# copy는 매우 중요