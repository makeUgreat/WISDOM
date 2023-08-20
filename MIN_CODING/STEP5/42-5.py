n = int(input())

cnt = 0
def abc(level,Sum):
    global cnt 
    
    if level == n:
        if Sum == 10:
            cnt += 1
        return
        
    
    for i in range(10):
        abc(level+1, Sum +(i+1)) 
    
abc(0,0)
print(cnt)