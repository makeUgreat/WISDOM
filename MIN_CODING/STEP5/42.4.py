coin = [10,40,60]
changes = int(input())

min_v = 21e8
def abc(level,changes):
    global min_v

    if changes == 0:
        if level < min_v:
            min_v = level
        return



    for i in range(3):
        if changes-coin[i] >= 0:
            abc(level+1,changes-coin[i])

abc(0,changes)
print(min_v)