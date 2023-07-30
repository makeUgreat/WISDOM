def find():
    y1, x1 = map(int,input().split())
    y2, x2 = map(int,input().split())
    for y in range(len(lsts)):
        for x in range(len(lsts[y])):
            if y == y1 and x == x1:            
                print(lsts[y][x],end=' ')
            if y == y2 and x == x2:
                print(lsts[y][x],end='')
            
            
            

lsts = [
    ['D','A','S'],
    ['Q','W','V'],
    ['R','T','Y']
]


find()

