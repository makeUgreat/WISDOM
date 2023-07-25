def BBQ(a,b):
    print(f'합:{a+b}')
    print(f'차:{a-b}')
    print(f'곱:{a*b}')
    print(f'몫:{a//b}')



user_input = map(int,input().split())
BBQ(*user_input)
