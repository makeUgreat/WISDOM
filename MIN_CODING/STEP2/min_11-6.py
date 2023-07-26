num = int(input())
lsts = [3,4,1,3,2,7,3]

flag = 0

for lst in lsts:
    if num == lst:
        flag += 1
        if flag >= 1:
            print("발견")
            break
if flag == 0:
    print("미발견")
    


# GPT 코드
num = int(input())
lsts = [3, 4, 1, 3, 2, 7, 3]

flag = False

for lst in lsts:
    if num == lst:
        flag = True
        break

if flag:
    print("발견")
else:
    print("미발견")
