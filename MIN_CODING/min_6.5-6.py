arr = list(map(ord,input().split()))
count = 0

for i in arr:
    if 48 <= i <= 57:
        count += 1
    
if count == 0:
    print("숫자미발견")
else:
    print(f'숫자{count}개발견')