lsts = []

for i in range(4):
    line = input()
    lsts.append(line)
    
    

line_len = []

for lst in lsts:
    line_len.append(len(lst))

line_len.sort()
print(*line_len)