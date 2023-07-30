lsts = []

for i in range(2):
    line = list(input())
    lsts.append(line)
    
counting = 0
max_len = []
for lst in lsts:
    if len(max_len) < len(lst):
        max_len.clear()
        max_len.append(lst)

    
for i in range(len(max_len[0])):
    try:
        if lsts[0][i] != lsts[1][i]:
            counting += 1
    except IndexError:
        pass
counting += abs(len(lsts[0]) - len(lsts[1]))
        
        
print(counting)


# gpt
'''
lsts = []

for i in range(2):
    line = list(input())
    lsts.append(line)

counting = 0

# 두 개의 리스트 길이를 바로 비교하고, 첫 번째 리스트가 더 길면 해당 리스트를 max_len으로 설정합니다.
max_len = lsts[0] if len(lsts[0]) > len(lsts[1]) else lsts[1]

# zip을 사용하여 두 개의 리스트를 병렬로 비교하고, 다른 값을 가진 경우 counting을 증가시킵니다.
for item1, item2 in zip(lsts[0], lsts[1]):
    if item1 != item2:
        counting += 1

# 두 개의 리스트 중 길이가 더 짧은 리스트의 나머지 요소들을 세어줍니다.
counting += abs(len(lsts[0]) - len(lsts[1]))

print(counting)
'''