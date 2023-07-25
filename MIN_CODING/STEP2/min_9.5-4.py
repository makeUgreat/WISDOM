lsts = [
    [10,3,20],
    [60,30,40],
    [20,30,40]
]

a, b = map(int,input().split())
count = 0
for k in range(a,b+1):
    for i in range(len(lsts)):
        count += lsts[i].count(k)

print(count)