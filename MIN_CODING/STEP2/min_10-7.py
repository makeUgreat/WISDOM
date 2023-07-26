def GOP(n1, n2):
    return n1 * n2

def SUM(n1, n2):
    return n1 + n2


n1, n2 = map(int,input().split())
gop_value = GOP(n1,n2)

n1, n2 = map(int,input().split())
sum_value = SUM(n1,n2)

if gop_value > sum_value:
    print('GOP>SUM')
elif sum_value > gop_value:
    print('GOP<SUM')
else:
    print('GOP==SUM')