nums = map(int,input().split())
lsts = []

for num in nums:
    line = [num + j for j in range(4)]
    lsts.append(line)


for lst in lsts:
    print(*lst)

