def even(value):
    value *= 2 
    printData(value)


def odd(value):
    value -= 10
    printData(value)

def printData(values):
    print(values)

a, b = map(int,input().split())
value = int(a/b) 
sum_value = a+b
if value % 2 == 0:
    even( value )
elif value % 2 == 1:
    odd( value )

printData(sum_value)

