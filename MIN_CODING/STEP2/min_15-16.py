ch1 = ord(input()) - 1

lsts = []

j = 2
k = 0
i = 4

while i >= 1:
    line = []
    k = i
    while i <= k + j:
        line.append(chr(ch1 + i))
        i += 1
    j -= 1
    i = int(i / 2) - 1
    lsts.append(line)

lst_index = 0
while lst_index < len(lsts):
    lst = lsts[lst_index]
    element_index = 0
    while element_index < len(lst):
        print(lst[element_index], end="")
        element_index += 1
    print()
    lst_index += 1