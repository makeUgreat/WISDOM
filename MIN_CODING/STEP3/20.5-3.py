st = input()

half_leng = len(st)//2

half_st = st[:half_leng]
rev_half_st = st[-half_leng:]

if half_st == rev_half_st:
    print('동일한문장')
else:
    print('다른문장')