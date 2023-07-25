char = ord(input())
lst = []
for j in range(3):
    line = []
    for i in range(5):
        line.append(chr(char))
        char += 1
    lst.append(line)
        
lst[2][2] = lst[2][2].lower()
print(lst[2][2])