flag = 0
for _ in range(3):
    st = list(input())
    
    if st.count('M'):
        flag = 1

if flag: print('M이 존재합니다')
else: print('M이 존재하지 않습니다')