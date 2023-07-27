lsts = ['D','A','T','A','P','O','W','E','R']
arr = []
a , b = map(int,input().split())

for i in range(a,b+1):
    arr.append(lsts[i])

print(*arr,sep='',end='')