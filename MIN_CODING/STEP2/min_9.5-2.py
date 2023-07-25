lsts = list(map(ord,input().split()))

count = lsts.count(65)
print(f'문자A는 {count}개발견')

for i in range(len(lsts)):
    if lsts[i] == 65:
        print(f'{i}번')
