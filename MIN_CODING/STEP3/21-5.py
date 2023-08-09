strs = []
max_len = ''
max_i = 0
for _ in range(3):
    line = input()
    strs.append(line)


for i in range(3):
    
    if len(strs[i]) > len(max_len):
        max_len = strs[i]
        max_i = i

tmp = strs[0]
strs[0] = max_len
strs[max_i] = tmp
        
for s in strs:
    print(s)