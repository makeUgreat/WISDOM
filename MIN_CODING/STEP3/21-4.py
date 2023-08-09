num = int(input())

def recursion(level):
    
    print(level,end='')
    

    if level == num:
        return

    for i in range(2):
        recursion(level+1)



recursion(0)