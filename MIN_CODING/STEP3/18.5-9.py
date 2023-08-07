st = input()

bucket = {}
for s in st:
    bucket[s] = bucket.get(s,0) + 1

lst = []
for key in bucket.keys():
    lst.append(key)

lst.sort()

print(*lst,end='')
