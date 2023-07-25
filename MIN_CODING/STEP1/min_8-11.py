def starBox():
    lst = [i for i in range(1,21) if i % 2 == 1]
    for i in lst:
        print(i,end=' ')


def macDoll():
    for i in ['H','G','F','E','D','C','B','A']:
        print(i,end=' ')


def copyBean():
    for i in range(-5,6):
        print(i,end=' ')





price = int(input())

if 3500 <= price <= 5000:
    starBox()
elif 2500 <= price <= 3500:
    macDoll()
else:
    copyBean()