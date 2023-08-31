st = list(map(ord,input()))
Len = len(st)

n = 0
end_pt = 0
empty_cnt = 0
while 1:
    st = list(map(chr,st))
    print(*st,sep='')

    st = list(map(ord,st))
    Sum = sum(st)

    for i in range(Len):
        if st[i] != 95:
            st[i] -= 1

            if st[i] < 65:
                st[i] = 95

    if Sum >= (95*Len):
        break

