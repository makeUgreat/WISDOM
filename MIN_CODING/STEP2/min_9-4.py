lsts = [3,4,2,5,7,9]
a, b = map(int,input().split())
tmp = 0

# swap
tmp = lsts[a]
lsts[a] = lsts[b]
lsts[b] = tmp 

print(*lsts,end=' ')
 
