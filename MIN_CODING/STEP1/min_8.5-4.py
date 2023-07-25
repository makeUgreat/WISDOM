lst = []
def input_func():
    ch1, ch2, ch3 = input().split()

    lst.append(ch3*4)
    lst.append(ch2*6)
    lst.append(ch1*7)
    
    result = ''.join(lst)
    print(result)

input_func()