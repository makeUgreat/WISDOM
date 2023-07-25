def getChar():
    ch1, ch2 = input().split()
    if ch1 > ch2:
        return ch1
    elif ch2 > ch1:
        return ch2
    
print(getChar())
    

