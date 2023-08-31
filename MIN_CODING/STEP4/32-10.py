N = int(input()) # N*N

arr = [list(map(int,input().split())) for _ in range(N)]
bit = [list(map(int,input().split())) for _ in range(N)]

lst = []
for i in range(N):
    for j in range(N):
        if bit[i][j] == 1:
            lst.append(arr[i][j])

ans = sorted(lst,key=lambda x: (-lst.count(x),x))
print(*ans)