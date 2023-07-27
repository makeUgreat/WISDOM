st1 = input()
st2 = input()
st3 = input()

# len_1, len_2, len_3 = len(st1), len(st2), len(st3)

# if len_1 > len_2 and len_1 > len_2:
#     print(st1)
# elif len_2 > len_1 and len_2 > len_3:
#     print(st2)
# elif len_3 > len_1 and len_3 > len_2:
#     print(st3)


max_length = max(len(st1),len(st2),len(st3))

if len(st1) == max_length:
    print(st1)
elif len(st2) == max_length:
    print(st2)
else:
    print(st3)
    
    