# strs = list(input())
# ch1 = input()
# ch2 = input()
# ch3 = input()


# print(f'{ch1}={strs.count(ch1)}')
# print(f'{ch2}={strs.count(ch2)}')
# print(f'{ch3}={strs.count(ch3)}')


strs = list(input())
ch1 = input()
ch2 = input()
ch3 = input()

ch1_count = 0
ch2_count = 0
ch3_count = 0

for str in strs:
    if str == ch1:
        ch1_count += 1
        continue
    if str == ch2:
        ch2_count += 1
        continue
    if str == ch3:
        ch3_count += 1
        continue

print(f'{ch1}={ch1_count}')
print(f'{ch2}={ch2_count}')
print(f'{ch3}={ch3_count}')