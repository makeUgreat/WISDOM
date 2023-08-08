def BBQ():
    global a
    global b
    nums = list(map(int,input().split()))

    a = max(nums)
    b = min(nums)

a = 0
b = 0
BBQ()

print(f'a={a}')
print(f'b={b}')