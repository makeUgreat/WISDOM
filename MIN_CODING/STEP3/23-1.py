name = list(input())

# 순열
# br = 4
# level = 3
path = [''] * 3
visited = [''] * 4 # branch  

def abc(level):
    
    if level == 3:
        for i in range(level):
            print(path[i],end='')
        print()
        return
    
    for i in range(4):
        if visited[i] == 1: continue
        visited[i] = 1
        path[level] = name[i]
        abc(level+1)
        visited[i] = 0

abc(0)