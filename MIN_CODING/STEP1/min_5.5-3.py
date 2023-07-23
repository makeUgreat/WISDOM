n1, n2 = map(int,input().split())

lst_1 = [n1]*5
lst_2 = [n2]*5

def PrintAll():
    print(*lst_1,sep='')
    print(*lst_2,sep='')

PrintAll()