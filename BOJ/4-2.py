row = ['','a','b','c','d','e','f','g','h']
col = [0,1,2,3,4,5,6,7,8]

chess = [ [0]*9 for _ in range(9) ]

def delta(y,x):
    global cnt
    direction = [(-2,1),(-2,-1),(2,1),(2,-1),
                 (1,-2),(1,2),(-1,-2),(-1,2)]

    for yy,xx in direction:
        dy = y + yy
        dx = x + xx

        if dy < 1 or dx < 1 or dy>=8 or dx>=8: continue
        cnt += 1

night = input()
y,x = row.index(night[0]), int(night[1])
cnt = 0
delta(y,x)

print(cnt)



