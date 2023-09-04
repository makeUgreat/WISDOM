from collections import deque
import sys
sys.stdin = open('input.txt','r')

S = int(input())
D = int(input())

visit = [False] * 200001
ans = 21e8
def bfs(now):
    global ans
    q = deque()
    q.append([now,0])
    visit[now] = True

    while q:

        now,cnt = q.popleft()

        if now == D:
            ans = cnt
            return

        if 0 <= now <= 100000 and not visit[now //2]:
            q.append([now//2,cnt+1])
            visit[now//2] = True
        if 0 <= now <= 100000 and not visit[now*2]:
            q.append([now*2,cnt+1])
            visit[now*2] = True
        if 0 <= now <= 100000 and not visit[now+1]:
            q.append([now+1,cnt+1])
            visit[now+1] = True
        if 0 <= now <= 100000 and not visit[now-1]:
            q.append([now-1,cnt+1])
            visit[now-1] = True


bfs(S)
print(ans)