st = input()

path = [''] * 3
def abc(level,start):

    if level==3:
        for i in range(level):
            print(path[i],end='')
        print()
        return
    
    for i in range(start,len(st)):
        path[level] = st[i]
        abc(level+1,i)

abc(0,0)