max_str = ['a']
for i in range(5):
    st1 = input()
    if len(st1) > len(max_str[0]):
        max_str.clear()
        max_str.append(st1)


print(*max_str)
