ch1, ch2 = input().split()

lsts = ['D','F','G','D','A','Q']
flag = 0

for lst in lsts:
    if ch1 <= lst <= ch2:
        flag = True
        
if flag:
    print("발견!!!")
else:
    print("미발견!!!")