print(10, 20 ,30) # 파라미터 위치 그대로 인자로 받아 출력

def prt_nums(a, b, c):
    print(a)
    print(b)
    print(c)
prt_nums(10,15,'c') # 위치대로 매개변수 대입 

x = [10, 20, 30]

prt_nums(*x) # 언패킹을 통해 요소 각각 풀어 대입 

print('---------------')
def print_numbers(*args):
    for arg in args:
        print(arg)
        
print(input().split())