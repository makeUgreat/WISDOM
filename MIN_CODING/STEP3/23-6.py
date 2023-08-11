cards = list(map(int,input()))
path = [0] * 4
# level = 4
# branch = 5
cnt = 0

def abc(level):
    global cnt
    if level == 4:
        flag = 1
        for i in range(3):
            if abs(path[i] - path[i+1]) > 3:
                flag = 0
        if flag:
            cnt += 1
        
        
        return
    
    for i in range(5):
        path[level] = cards[i]
        abc(level+1)

abc(0)
print(cnt)