# br = 3
# lv = 2
node = ['A','B','C']
path = [''] * 2

def recursion(level):

    if level == 2:
        for i in range(level):
            print(path[i],end='')
        print()
        return
    
    for i in range(3):
        path[level] = node[i]
        recursion(level+1)


recursion(0)