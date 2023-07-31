lsts = [
    [5,1,4,2,6],
    [3,5,0,0,7],
    [9,9,8,3,1]
]

num = int(input())

count = 0
for lst_ in lsts:
    for _ in lst_:
        if _ > num:
            count += 1

print(f'{count}개')
