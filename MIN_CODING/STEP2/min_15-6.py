st1 = input()
check_lst = []

for i in st1:
    
    if i.isupper():
        check_lst.append(1)
    elif i.islower():
        check_lst.append(0)
        
        
flag = False
for i in range(len(check_lst)-1):
    if check_lst[i] == check_lst[i+1]:
        flag = True
        
if flag:
    print('일반문장')
else:
    print('개구리문장')