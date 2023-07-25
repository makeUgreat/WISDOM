lsts = [
    [3,5,14],
    [2,3,9],
    [6,2,7]
]

num = int(input())
count = 0
for lst in lsts:
    for i in lst:
        if i % num == 0:
            count += 1
            
print(count)