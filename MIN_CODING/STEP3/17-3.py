lsts = [
    [3,5,9],
    [4,2,1],
    [1,1,5]
]

lsts2 = []
for i in range(3):
    line = list(map(int,input().split()))
    lsts2.append(line)


# lsts랑 lsts2 비교

sum_ = 0
for i in range(len(lsts2)):
    for j in range(len(lsts2[i])):

        if lsts2[i][j] == 1:
            sum_ += lsts[i][j]

print(sum_)