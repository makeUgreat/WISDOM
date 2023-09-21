import sys
sys.stdin = open('input.txt','r')

from collections import deque

n,k = map(int,input().split())
visit = [False] * 200001

def bfs(start):
    q = deque()
    q.append([start,0])
    visit[start] = True

    while q:
        now,cnt = q.popleft()
        print(now,cnt)
        if now == k:
            return cnt

        if 2*now <= 200001 and not visit[2*now]:
            visit[2*now] = True
            q.append([2*now,cnt])
        if now-1 >= 0 and not visit[now-1]:
            visit[now-1] = True
            q.append([now-1,cnt+1])
        if now+1 <= 100001 and not visit[now+1]:
            visit[now+1] = True
            q.append([now+1,cnt+1])

ans = bfs(n)
print(ans)