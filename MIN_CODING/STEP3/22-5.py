n = int(input()) # branch
# level 4
path = [0] * 4

def recursion(level):
    
    if level == 4:
        for i in range(level):
            print(path[i],end='')
        print()
        return
    
    for i in range(n):
        path[level] = (i+1)
        recursion(level+1)

recursion(0)