lsts = [
    [1,3,6,2],
    [4,2,4,5],
    [6,3,7,3],
    [1,5,4,6]
]

num = int(input())
select = []

for i in range(len(lsts)):
    for j in range(len(lsts[i])):
        if lsts[i][j] > num:
            select.append(lsts[i][j])
            
            

print(*select)