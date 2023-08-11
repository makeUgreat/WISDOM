# level = 3
# branch = 4

node = ['A','B','C','D']
path = [''] * 3 
set_list = []
cnt = 0
st = input()
def abc(level):
    global cnt
    
    if level == 3:
        cnt += 1
        if ''.join(path) == st:
            print(f'{cnt}번째')

        return

    for i in range(4):
        path[level] = node[i]
        abc(level+1)

abc(0)


