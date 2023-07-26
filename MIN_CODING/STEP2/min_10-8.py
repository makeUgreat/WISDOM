def pingpong(get_stone):
    tong = get_stone

    return tong + 10


stone = int(input())

ret = pingpong(stone)
print(ret)