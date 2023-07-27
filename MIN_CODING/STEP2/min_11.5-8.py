a, b, c = map(int,input().split())

lsts = [
    [3,1,6],
    [7,8,4],
    [9,2,3]
]

lsts[a][b] = c 
max_value = []
min_value = []

for lst in lsts:
    max_value.append(max(lst))
    min_value.append(min(lst))

print(max(max_value) + min(min_value))
    