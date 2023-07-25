ch1, ch2, n1 = input().split()
n1 = int(n1)
gap = ord(ch2) - ord(ch1)


for i in range(n1):
    for j in range(gap + 1):
        print( chr(ord(ch1) + j),end='' )
    print()