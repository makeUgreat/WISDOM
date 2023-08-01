lsts = [4,7,1,3,5]
tmp = 0

for i in range(len(lsts)):
    for j in range(i+1,len(lsts)):
        if lsts[i] > lsts[j]:
            tmp = lsts[i]
            lsts[i] = lsts[j]
            lsts[j] = tmp


print(lsts)

