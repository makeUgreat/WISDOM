x, y = input().split()

gap = ord(y) - ord(x)
for j in range(4):
    for i in range(gap+1):
        print(chr(ord(x) + i),'',end='') 

    print()