lsts = []

for _ in range(2):
    line = list(input())
    lsts.append(line)
    

result = []

for lst in lsts:
    result.extend(lst)
    

print(''.join(result))