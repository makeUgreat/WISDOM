def isSame(name1, name2):
    for i in range(len(name1)):
        if len(name1) != len(name2):
            return 0
        if name1[i] != name2[i]:
            return 0

    return 1

name1 = list(input())
name2 = list(input())

if isSame(name1, name2):
    print('동명')
else:
    print('남남')
