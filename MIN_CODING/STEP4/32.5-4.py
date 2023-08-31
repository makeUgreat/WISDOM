N = int(input())
guess = [0]+[i for i in range(1,51)]

high,low = 50,1
flag = 1
for _ in range(N):
    order = list(input().split())
    now = int(order[0])
    up_down = order[1]

    if up_down == 'UP':
        low = now+1


    elif up_down == 'DOWN':
        high = now-1

    if low > high:
        print('ERROR')
        flag = 0
        break

    if low == high:
        print(guess[low])
        flag = 0
        break

if flag: print(f'{guess[low]} ~ {guess[high]}')




