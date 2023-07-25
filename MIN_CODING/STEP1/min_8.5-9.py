ch1, ch2 = input().split()

lst = []
for k in range(3):
    line = []
    for i in range(4):
        line.append(ch1)
    for j in range(2):
        line.append(ch2)
    lst.append(line)


for i in lst:
    for j in i:
        print(*j,end='')
    print()


