# br = 2 [O,X]
# level = n

n = int(input())
maybe = ['x','o']
path = [''] * n 

def abc(level):

    if level == n:
        for i in range(level):
            print(path[i],end='')
        print()
        return
    
    for i in range(2):
        path[level] = maybe[i]
        abc(level+1)


abc(0)