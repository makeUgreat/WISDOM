class calculrator():
    numberOfCalcul = 0

    def __init__(self):
        self.result = 0
        calculrator.numberOfCalcul += 1
    
    def getsum(self,value):
        self.result += value
        return self.result
    

cal1 = calculrator()
cal2 = calculrator()

print(cal1.getsum(3))
print(cal1.getsum(4))
print(cal1.getsum(5))



print(calculrator.numberOfCalcul)
# 클래수 변수 사용시 주의점!!
# 클래스 변수 값을 변경할 때에는 반드시 항상!! 클래스명.클래스인수 형식으로 접근해야 한다.

calculrator.numberOfCalcul = 6
print('클래스 값을 바꿔서 모든 cal 클래스의 인스턴스들은 6값을 받음')
print(cal1.numberOfCalcul)
print(cal2.numberOfCalcul)

print('인스턴스에 있는 numberOfCalcul 의 값을 바꾸면 그 인스턴스의 값만 바뀜')
cal1.numberOfCalcul = 10
print(cal1.numberOfCalcul)
print(cal2.numberOfCalcul)





def call_name(name):
    print(name)

def call_age(age):
    print(age)

call_name('KJM')
call_age(28)