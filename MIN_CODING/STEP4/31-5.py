n = int(input())
arr = list(input().split())

result = ['']*2
visit = [False]*7
cnt = 0
def dfs(level):
    global cnt

    if level == 2:
        if arr.index(result[0]) >= arr.index(result[1]):
            return
        if ''.join(result) == 'HITSMUSIC':
            cnt += 1
        return

    for i in range(n):
        if visit[i]: continue
        visit[i] = True
        result[level] = arr[i]
        dfs(level+1)
        visit[i] = False
dfs(0)
print(cnt)