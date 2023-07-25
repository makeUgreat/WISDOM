def BBQ(x):
    if 0 < x < 5:
        print("초기값")
    elif 6 < x < 10:
        print("중간값")
    else:
        print("알수없는값")
    

x = int(input())

if x == 3 or x == 5 or x == 7:
    for i in range(1,11):
        print(i,end='')
elif x == 0 or x == 8:
    for i in range(10,0,-1):
        print(i,end='')
else:
    BBQ(x)