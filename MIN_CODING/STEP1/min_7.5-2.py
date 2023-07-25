arr = []
for i in range(6):
    arr.append(0)
   
indexes = map(int,input().split())

for i in indexes:
    arr[i] = 1
    
print(*arr)