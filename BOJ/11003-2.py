import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, L = map(int, input().split())
nums = list(map(int, input().split()))

q = deque()
ans = []

for i in range(N):
    # 현재 값보다 큰 값을 가진 인덱스 제거
    while q and q[-1][0] > nums[i]:
        q.pop()
    # 현재 윈도우 범위 밖의 인덱스 제거
    while q and q[0][1] < (i - L + 1):
        q.popleft()

    q.append((nums[i], i))
    ans.append(str(q[0][0]))
    print(q)

# 한 번에 출력
print(' '.join(ans))
