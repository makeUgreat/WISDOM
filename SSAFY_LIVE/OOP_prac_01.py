# 클래스 정의
class Person: # 클래스는 파스칼 케이스로 지음(단어 맨앞마다 대문자)
    # 속성(변수)
    blood_color = 'red'

    #메서드
    def __init__(self, name):
        self.name = name  # 인스턴스 변수,인스턴스마다 별도로 유지되는 변수,

    # __xxx__ : 매직메서드, 개발자가 직접 호출하지 않음. 
    # 안보이는 어딘가에서 혼자 기능 
    # __init__ : 생성자 메서드, 객체를 생성할 때 자동으로 호출되는 특별한 메서드, 객체의 초기화를 담당


    def singing(self):
        return f'{self.name}가 노래합니다.'


# 인스턴스 생성
singer1 = Person('iu') # init 함수에서 name이라는 인자를 받기 떄문에 꼭 매개변수를 하나 넣어줘야함
singer2 = Person('BTS')


# 메서드 호출
print(singer1.singing()) 
print(singer2.singing())

# 속성(변수) 사용
print(singer1.blood_color)
print(singer2.blood_color)


