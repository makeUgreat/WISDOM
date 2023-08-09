a,b = map(int,input().split())

def abc(a,b):

    if a == b:
        print(a,end=' ')
        return
    
    print(a,end=' ')
    abc(a+1,b)
    print(a,end=' ')

abc(a,b)