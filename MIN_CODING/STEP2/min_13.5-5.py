lsts = [
    ['4','5','7','1','3','2'],
    ['D','F','Q','W','G','Z']
]

num = input()

for lst in lsts:
    if num in lst:
        print(lsts[1][lst.index(num)])


