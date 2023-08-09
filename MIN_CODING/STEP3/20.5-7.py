st = input()
path = []
def stair(index):
    path.append(st[index])
    print(*path,sep='')
    if index == len(st)-1:
        return
    
    stair(index+1)



stair(0)