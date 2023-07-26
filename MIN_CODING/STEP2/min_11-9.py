lsts = list(input())
big = []
small = []

for lst in lsts:
    if lst.isupper():
        big.append(lst)
    elif lst.islower():
        small.append(lst)
        

print('big=',*big,sep='')
print('small=',*small,sep='')