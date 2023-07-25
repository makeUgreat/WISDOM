n1, n2 = map(int,input().split())

gap = n2 - n1
if gap < 0:
    gap = -gap

if gap % 2 == 0:
    print('짝사랑만')
else:
    print('고백한다')