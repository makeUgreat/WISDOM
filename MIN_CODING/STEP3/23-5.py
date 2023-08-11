member = ['E','W','A','B','C']
st = input()
path = [''] * 4
visited = [0] * 5

# level = 4
# br = 5
def abc(level):
    
    if level == 4:
        
        if st not in path:
            for i in range(level):
                print(path[i],end='')
            print()
        return
    
    for i in range(5):
        if visited[i] == 1: continue
        visited[i] = 1
        path[level] = member[i]
        abc(level+1)
        visited[i] = 0
        


abc(0)