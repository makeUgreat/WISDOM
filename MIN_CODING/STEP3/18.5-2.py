nums = map(int,input().split())

cnt = {}
for num in nums:
    cnt[num] = cnt.get(num,0)+1

exist = 0
for value in cnt.values():
    if value >= 2:
        exist = 1
        break

if exist:
    print("도플갱어 발견")
else:
    print("미발견")