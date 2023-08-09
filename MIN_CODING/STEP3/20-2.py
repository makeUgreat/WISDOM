n = int(input())

def recursion(level):
    
    if level == 0:
        print(level,end=' ')
        return
    print(level,end=' ')

    recursion(level-1)
    print(level,end=' ') 
    
    



recursion(n)