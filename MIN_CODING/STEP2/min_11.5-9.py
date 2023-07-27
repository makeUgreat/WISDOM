line = list(map(int,input().split()))
line.reverse()
lsts = []

for i in range(0,len(line),3):
    lsts.append(line[i:i+3])


arr = []
for lst in lsts:
    for ls in lst:
        arr.append(ls)

tmp = 0
tmp = arr[0]
arr[0] = arr[5]
arr[5] = tmp

print(*arr)