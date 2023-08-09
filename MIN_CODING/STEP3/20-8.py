num = int(input())


def abc(get_num):

    if get_num == 0:
        return

    abc(get_num//2)
    print(get_num,end=' ')


abc(num)