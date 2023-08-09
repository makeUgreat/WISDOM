st = input()

def recursion(index):

    if index == len(st):
        print()
        return

    print(st[index],end='')    
    recursion(index+1)
    print(st[index],end='')


recursion(0)