import sys
sys.stdin = open('input.txt','r')

f,s,g,u,d = map(int,input().split())


def dfs(now,cnt):
    global flag

    if now == g:
        flag = 0
        print(cnt)
        return

    if now > f or now > now+d:
        return
    if now < 1 or now < now-u:
        return

    # 가려는 층이 현재 층보다 위면
    if g > now:
        dfs(now+u,cnt+1)
    # 가려는 층이 현재 층보다 아래면
    if g < now:
        dfs(now-d,cnt+1)


flag = 1
dfs(s,0)
if flag: print('use the stairs')