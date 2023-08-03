ch = input()

lsts = []
for i in range(5):
    line = [ chr((65+j) + (i*5)) for j in range(5) ]  # A 65 Z 90
    lsts.append(line)


for i in range(len(lsts)):
    for j in range(len(lsts[i])):

        if lsts[i][j] == ch:
            print(f'{i-2},{j-2}')


# for i, row in enumerate(lsts):  
#     for j, char in enumerate(row):
#         if char == ch:
#             return f"{i-2},{j-2}"