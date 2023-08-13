y_list = []
x_list = []

for _ in range(3):
    y,x = map(int,input().split())
    
    y_list.append(y)
    x_list.append(x)
flag = 0
for i in range(2):
    if y_list[i] == y_list[i+1]:
        flag = 1
    if x_list[i] == x_list[i+1]:
        flag = 1
        
if flag:
    print('위험')
else: print('안전')        