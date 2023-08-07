win = [
    [3,5,1],
    [4,2,6]
]

people = list(map(int,input().split()))


lst = []
for row in win:
    lst.extend(row)

for num in people: 
    if num in lst:
        print(f'{num}번 합격')
    else:
        print(f'{num}번 불합격')