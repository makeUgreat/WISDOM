def do(get_order):
    global y
    global x

    if get_order == 'up':
        y -= 1

    if get_order == 'down':
        y += 1

    if get_order == 'left':
        x -= 1

    if get_order == 'right':
        x += 1

    if get_order == 'click':
        print(f'{y},{x}')
    
        

y,x = 5,5
N = int(input())

for _ in range(N):
    do(input())

    