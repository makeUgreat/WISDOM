# level = n
# branch = 3 

n = int(input())
choco = ['A','B','C']
path = [''] * n
cnt = 0

def abc(level):
    global cnt 
    
    if level == n:
        flag = 1 
        for i in range(n-2):
            if path[i] == path[i+1] and path[i+1] == path[i+2]:
                flag = 0
        
        if flag:
            cnt += 1
            
            
        
        return
    
    for i in range(3):
        path[level] = choco[i]
        abc(level+1)
    
abc(0)
print(cnt)