char = input().split()  #65 ~ 90
count = sum(1 for ii in char if ii.isupper())
if count == 3:
    print("풍족하다")
elif 1 <= count <= 2:
    print("적절하다")
else:
    print("부족하다")