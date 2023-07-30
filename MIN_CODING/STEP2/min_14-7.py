lsts = list(map(int,input().split()))

lsts.sort(reverse=True)

print(*lsts,sep='',end='')