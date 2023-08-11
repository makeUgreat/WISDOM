strings = []

for _ in range(4):
    line = input()
    strings.append(line)

max_len = -21e8
min_len = 21e8
max_i = 0
min_i = 0
for i in range(4):
    if len(strings[i]) > max_len:
        max_len = len(strings[i])
        max_i = i
    
    if len(strings[i]) < min_len:
        min_len = len(strings[i])
        min_i = i

print(f'긴문장:{max_i}')
print(f'짧은문장:{min_i}')


