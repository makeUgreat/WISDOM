def isExist(get_char,get_lsts):
    for row in get_lsts:
        if get_char in row:
            return 1
        



lsts = [
    ['G','K','T'],
    ['P','A','C']
]

chars = input().split()
cnt = 0
for char in chars:
    if isExist(char,lsts):
        cnt += 1

if cnt >= 2:
    print('대발견')
elif cnt < 0:
    print('미발견')
else:
    print('중발견')

