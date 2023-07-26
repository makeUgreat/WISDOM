def sum(a, b):
    return a + b

def comp(a, b):
    return a - b

def print_func(t1, t2):
    
    print(f'합:{t1}')
    print(f'차:{t2}')
    
    
    
a, b = map(int,input().split())
print_func(sum(a,b) , comp(a,b))