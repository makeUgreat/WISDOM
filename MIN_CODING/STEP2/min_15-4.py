st1 = input()
st2 = input()

st2 = ''.join(list(reversed(st2)))
if st1 == st2:
    print('거울문장')
else:
    print('거울문장아님')