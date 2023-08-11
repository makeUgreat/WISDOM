me = 1

for i in range(5):

    st = input() 

    if st == 'up':
        me += 1

    if st == 'down':
        me -= 1

    
if me < 0: 
    me = abs(me)+1 # 0층은 없으니까
    print(f'B{me}')
else:
    print(me)
