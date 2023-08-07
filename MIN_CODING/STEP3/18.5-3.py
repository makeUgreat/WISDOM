st = input()

cnt = {}

for s in st:
    cnt[s] = cnt.get(s,0) + 1

max_ = -21e8
max_key = 0
for key, value in cnt.items():
    if value > max_:
        max_ = value
        max_key = key

print(max_key)