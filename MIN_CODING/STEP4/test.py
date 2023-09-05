from collections import deque
import sys
sys.stdin = open("input.txt","r")

C = int(input())
cumputer = [i for i in range(C+1)]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
q = deque()


q.append(arr[0][0])
cnt = 0
used = [0] * (N+1)

answer = []
while q:
    node = q.popleft()
    # print(answer)
    # print(set(answer))

    for i in range(N):
        if used[i] == 1: continue
        used[i] = 1
        q.append(arr[i][1])
        answer.append(arr[i][1])

print(len(set(answer))-1)
