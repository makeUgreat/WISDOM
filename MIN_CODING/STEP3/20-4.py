def abc(level):

    if level == n+6:
        print(level,end=' ')
        return
    

    abc(level+2)
    print(level,end=' ')


n = int(input())
abc(n)