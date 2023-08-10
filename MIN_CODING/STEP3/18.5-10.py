st = input()

cnt = {}
for s in st:
    cnt[s] = cnt.get(s,0) + 1
    
sorted_items = sorted(cnt.items())
for key,value in sorted_items:
    print(f'{key}:{value}')