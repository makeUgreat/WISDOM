# 다중 상속
# 두 개 이상의 클래스를 상속 받는 경우
# 상속받은 모든 클래스의 요소를 활용 가능함
# 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨 

# 다중 상속 예시

class Person:
    gene = 'XXXX'

    def __init__(self,name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}' 


class Mom(Person):
    gene = 'XX'

    def __init__(self,name):
        super().__init__(name)

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def __init__(self,name):
        super().__init__(name)

    def walk(self):
        return '아빠가 걷기'


class Firstchild(Dad,Mom):  # .super()로 불러오면 상속 순서대로 불러옴 

    person_gene = Person.gene
    dad_gene = Dad.gene


    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'
    


baby1 = Firstchild('아가')
print(baby1.cry())
print(baby1.swim())
print(baby1.walk())
print(baby1.gene)
print(baby1.person_gene)
print(baby1.dad_gene)


    

# 상속 관련 함수와 메서드

# .mro()
#  Method Resoultuon Order
#  해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
#  기존의 인스턴스 -> 클래스 순으로 이름공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스로 확장

print(Firstchild.mro())
