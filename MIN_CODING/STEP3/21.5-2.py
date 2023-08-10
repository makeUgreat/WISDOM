arr = [
    [3,4,1,5],
    [3,4,1,3],
    [5,2,3,6]
]


Sum = []
index = int(input())
for ar in zip(*arr):
    Sum.append(sum(ar))


print(Sum[index])