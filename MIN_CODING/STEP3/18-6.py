town = [
    ['C','D','A'],
    ['B','M','Z'],
    ['Q','P','O']
]

black = list(input())

one_town = []
# town 1차원으로 풀기

for t in town:
    one_town.extend(t)

cnt = 0
for one in one_town:
    if one in black:
        cnt += 1

print(f'{cnt}명')
