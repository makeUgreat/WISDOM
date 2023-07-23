incre_lst = []
decre_lst = []

x = input()

if 69 <= ord(x) <= 86: # E <= x <= V
    for i in range(5):
        incre_lst.append( chr( ord(x)+i ) )
        decre_lst.append( chr( ord(x)-i ) )
    
    print(*incre_lst,sep='',end='')
    print()
    print(*decre_lst,sep='',end='')