name = list(input())
path = [''] * 4

cnt = 0
def abc(level):
    global cnt
    
    if level == 4:
        flag = 1
        for j in range(3):
            if path[j] == 'T' and path[j+1] == 'B': 
                flag = 0
            if path[j] == 'B' and path[j+1] == 'T':
                flag = 0
        
        if flag:
            cnt += 1
        return
    
    
    for i in range(4):
        path[level] = name[i]
        abc(level+1)
        
abc(0)
print(cnt)