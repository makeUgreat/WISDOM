ch1 = input()
gap = ord(ch1) - 97

for i in range(gap+1):
    print( chr(ord(ch1) - i),end=''    )