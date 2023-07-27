# Inheritance, 상속
# 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것

# 상속이 필요한 이유

# 1. 코드 재사용
# 새로 작성할 때 기존 클래스를 재사용함으로서 중복된 코드를 줄일 수 있음

# 2. 계층 구조
# 상속을 통해 클래스들간 계층구조를 형성할 수 있음(부모<->자식)

# 3. 유지 보수 용이
# 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수가 용이해짐

# 클래스 상속

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def talk(self):
        print(f'안녕, 난 {self.name}이야.')

class Professor(Person):
    def __init__(self, name, age, department):
        Person.__init__(self,name,age)
        self.depatrment = department

class Student(Person):
    def __init__(self, name, age, gpa):
        #Person.__init__(self,name,age)
        super().__init__(name,age) # 부모클래스의 메서드를 호출하기 위해 사용되는 내장 함수
        self.gpa = gpa



p1 = Professor('박교수',  49, '컴공')
s1 = Student('김학생',20,3.5)

p1.talk()
s1.talk()