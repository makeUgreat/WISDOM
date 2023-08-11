level = int(input())
path = [''] * level

node = ['B','G','T','K']

def abc(n):
    
    if n == level:
        for i in range(level):
            print(path[i],end='')
        print()
        return
    
    for i in range(4):
        path[n] = node[i]
        abc(n+1)    
    

abc(0)