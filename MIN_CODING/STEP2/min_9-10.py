def checkChar(ch1):
    if ch1.isupper():
        print("대",end='')
    elif ch1.islower():
        print("소",end='')



lsts = input().split()

for i in lsts:
    checkChar(i)
