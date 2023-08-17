#level = n 
#br = 2 

n = int(input())
path = [''] * n
name = ['o','x']

def abc(level):

    if level == n: 
        for i in range(n):
            print(path[i],end='')
        print()
        return

    for i in range(2):
        path[level] = name[i]
        abc(level+1)

abc(0)
