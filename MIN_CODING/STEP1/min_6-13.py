a, b, c = map(int,input().split())

for i in range(c):
    for j in range( (b-a) + 1):
        print( a + j,'',end='' )
    
    print()