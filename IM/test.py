name = ' ABCDE    FG'

def postorder(now):

    if now > len(name)-1: return

    postorder(now*2)
    print(name[now],end=' ')
    postorder(now*2+1)

postorder(1)
