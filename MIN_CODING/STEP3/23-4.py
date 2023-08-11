# level = 3
# branch = 5 
n = int(input())
member = ['B','T','S','K','R']
visited = [0] * 5
path = [''] * n
cnt = 0


def abc(level):
    global cnt 
    if level == n:
        flag = 1
        if 'S' not in path:
            flag = 0
            
        if flag: cnt += 1

        return
    
    for i in range(5):
        if visited[i] == 1: continue
        path[level] = member[i]
        visited[i] = 1
        abc(level+1)
        visited[i] = 0


abc(0)
print(cnt)