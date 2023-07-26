def yesOrNo():
    num = int(input())

    if num % 3 == 0:
        return 7
    if num % 3 == 1:
        return 35
    if num % 3 == 2:
        return 50
    

print(yesOrNo())