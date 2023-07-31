lsts = []
for i in range(3):
    line = [ 12-(4*i) - j for j in range(4) ]
    lsts.append(line)

num = int(input())

# line = [7] * 4
# lsts.remove(lsts[num-1])
# lsts.insert(num-1, line)
# =>
lsts[num - 1] = [7] * 4
# 인덱스로 넣어주면 값이 '대체'


for lst in lsts:
    print(*lst)