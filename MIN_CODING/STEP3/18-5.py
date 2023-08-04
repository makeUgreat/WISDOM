st1 = list(input())

bucket = {}

for st in st1:
    bucket[st] = bucket.get(st,0) + 1


max_v = -21e8
tmp_key = 0
for key,value in bucket.items():
    if value > max_v:
        max_v = value
        tmp_key = key


print(tmp_key)
    