lsts_1 = [2, 1, 2, 4 ,5]

lsts_2 = [
    [2, 5, 3],
    [4, 5, 7],
    [8, 7, 2]
]

num = int(input())

count = 0
count += lsts_1.count(num) 

for i in range(len(lsts_2)):
    count += lsts_2[i].count(num)

print(count)