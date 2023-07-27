# 문법 에러
# 프로그램의 구문이 올바르지 않은 경우 발생


# Invalid syntax, 문법오류
# cannot assign to literal, 잘못된 할당(숫자에 숫자 할당 등)
# EOL(End of Line) while scanning string literal
# EOF(End of File) unexpected EOF while parsing 


# 예외, Exception
# @ 프로그램 '실행 중' 감지 되는 에러(대부분)

# Built-in Exceptions, 예외 상황을 나타내는 예외 클래스

# ZeroDivisionError : 0으로 나누는 경우

# NameError  : 지역 또는 전역 이름을 찾을 수 없을 때



# TypeError : 타입 불일치
# : takes at least 1 positional arguments , 인자누락
# : takes at most 2 arguments(3 given), d인자 초과
# : Population must be a sequence, 인자 타입 불일치


# ValueError 
# 연산이나 함수에 문제가 없지만 부적절한 값을 가진 인자를 받았고
# 상황이 IndexError 처럼 더 구체적인 예외로 설명되지 않는 경우 발생

# indexError
# 시퀀스 인덱스가 범위를 벗어날 때 발생

# KeyError
# 딕셔너리에 해당 키가 존재하지 않는 경우

# ModuleNotFoundError
# 모듈을 찾을 수 없을 때 발생

# ImportError
# 임포트 하려는 이름을 찾을 수 없을 때 발생

# KeyboardInterrupt
# 사용자가 Control-C 또는 Delete를 누를 떄 사용
# 무한루프 시 강제 종료

# Indentation Error 
# 잘못된 들여쓰기와 관련된 문법 오류


# @@@@@@@@@@ 예외처리

# try-except 구조
# try 블록 안에는 예외가 발생할 수 있는 코드를 작성
# except 블록 안에는 예외가 발생했을 때 처리할 코드를 작성
# 예외가 발생하면 프로그램 흐름은 try블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동


try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다')


try:
    num = int(input('숫자입력 : '))
except ValueError:
    print('숫자가 아닙니다')


try:
    num = int(input('100을 나눌 값을 입력해: '))
    print(100 / num)
except ValueError: # (ValueError, ZeroDivisionError)
    print('숫자를 입력하라고')
except ZeroDivisionError:
    print('0으로 어떻게 나누니으이그')
except: # 그 외 예상치 못한 에러
    print('대체 뭘 한거니')