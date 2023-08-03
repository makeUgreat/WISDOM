# def isCount(get_char,get_vect):
#     for i in get_vect:
#         if i == get_char:
#             return 1
#     return 0

# vect = ['B','T','K','I','G','Z']


# cnt = 0
# target = input().split()

# for char_ in target:
#     if isCount(char_,vect):
#         cnt += 1

# print(cnt)
def isCount(get_char,get_vect):
    if get_char in get_vect:
        return 1

vect = ['B','T','K','I','G','Z']
target = input().split()

cnt = 0
for char_ in target:
    if isCount(char_,vect):
        cnt += 1

print(cnt)