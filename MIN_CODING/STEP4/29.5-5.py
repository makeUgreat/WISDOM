arrs = []

for _ in range(4):
    row = list(map(int,input().split()))
    arrs.append(row)


cnt = 0
max_v = -21e8 
def dfs(level):
    global cnt, max_v

    if level == 4:
        if max_v < cnt:
            max_v = cnt
        return

    for i in range(5):
        
        if arrs[level][i] == 1:
            cnt += 1
            if cnt == 1:
                print( f'({level},{i})')
        dfs(level+1)
        



dfs(0)