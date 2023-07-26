input_nums = list(map(int,input().split()))
lsts = []

# lsts.append(input_nums[0:3])
# lsts.append(input_nums[3:6])

for i in range(0, len(input_nums), 3):
    lsts.append(input_nums[i:i+3])
    
# for i in range( len(lsts) ):
#     for j in range( len(lsts[i]) ):
#         if lsts[i][j] == 0:
#             lsts[i][j] = '#'


for lst in lsts:
    for i in lst:
        if i == 0:
            print('#',end='')
            continue
        print(i,end='')
    print()
        