a, b = map(int,input().split())
arr = []

for i in range(a,a+3):
    arr.append(i)

for j in range(b-2,b+1):
    arr.append(j)

print(*arr,sep=' ')