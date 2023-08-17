from collections import deque
name="ABCD"
arr=[[0,1,1,0],
    [0,0,1,1],
    [0,1,0,1],
    [0,0,0,0]]

used=[0]*4
ans=[]
def bfs(start):
    global ans
    q=deque()
    q.append(start)

    while q:
        now=q.popleft()
        ans.append(name[now])
        for i in range(4):
            if arr[now][i]==1 and used[i]==0:
                used[i]=1
                q.append(i)

used[0]=1 #탐색 시작 인덱스에 해당하는 used에 1체크
bfs(0)
print(*ans)
