lst = ['G','K','G']

line = input().split()
lst.extend(line)

cnt = {}
for element in lst:
    cnt[element] = cnt.get(element,0) + 1

exist = 0
for values in cnt.values():
    if values >= 3:
        exist = 1
        break


if exist:
    print("있음")
else:
    print("없음")