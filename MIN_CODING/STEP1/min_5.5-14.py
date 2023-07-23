a, b = map(int,input().split())
lst = []
for i in range(a,b+1):
    lst.append(i)

print(*lst,sep='')