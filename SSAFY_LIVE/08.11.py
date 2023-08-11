
arr=[[3,5,9,6],
     [7,-8,1,6],
     [-10,2,3,9],
     [5,1,2,8],
     [4,7,1,8]]



cnt = 0
visited =[0] * 4
def dfs(level,sum):
    global cnt 
    
    if level == 4:
        if sum >= 30:
            cnt += 1
            
        return
    
    # for i in range(4):
    for j in range(-1,2):
        if j >= 0 and j < 4:
            dfs(level+1, sum + arr[level][j])

print(cnt)