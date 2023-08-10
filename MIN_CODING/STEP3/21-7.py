st = input()

len_st = len(st)

def abc(level):

    if level == 1:
        print(level,end=' ')
        return
    
    print(level,end=' ')

    abc(level-1)

    print(level,end=' ')

abc(len_st)