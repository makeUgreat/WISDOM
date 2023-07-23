a,b = map(int,input().split())
arr = []

i = a
count = 0
while count <= 4:
    arr.append(i)
    i += b
    count += 1

print(*arr)