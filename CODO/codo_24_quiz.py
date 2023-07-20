path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'

path = path.split('\\')
filename = path[-1]
print(filename)

"""
문자열 앞에 r 또는 R을 붙이면 raw 문자열이 됩니다. 이 raw 문자열은 이스케이프 시퀀스를 그대로 저장할 때 사용합니다. 즉, 다음과 같이 \를 \\로 두 번 쓰지 않고 한 번만 써도 됩니다.

>>> print(r'C:\Users\dojang\AppData\Local\Programs\Python\Python36-32\python.exe')
C:\Users\dojang\AppData\Local\Programs\Python\Python36-32\python.exe
raw는 가공되지 않고 있는 그대로라는 뜻입니다. 따라서 이스케이프 시퀀스를 문자 그대로 표현합니다. 다음과 같이 raw 문자열에 제어 문자를 입력해보면 제어 문자가 동작하지 않는 것을 볼 수 있습니다.

>>> print(r'1\n2\n3\n')
1\n2\n3\n
"""
