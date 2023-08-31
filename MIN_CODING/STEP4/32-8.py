N = int(input())

lst = []

for _ in range(N):
    na = input()
    name = list(na)

    if name[0].isupper():
        if all(name[c].islower() for c in range(1,len(name))):
            lst.append(na)
            continue

    for i in range(len(name)):
        # 대소문자 섞여 있으면
        if name[i].isupper():
            if any(char.islower() for char in na):
                name = [char.upper() for char in na]
                break
       # 소문자로만 이루어진 회원
        else:
            name[0] = name[0].upper()

    lst.append(''.join(name))


lst.sort()
for l in lst:
    print(l)