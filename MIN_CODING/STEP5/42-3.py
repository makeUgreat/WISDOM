# branch = 5
# max_level = 15  최대 30글자니까 최소 문장이 2

sts = ['BTS','SBS','BS','CBS','SES']

target = input()
min_v = 21e8

real_st =[]
cnt = 0
for st in sts:
    if st in target:
        real_st.append(st)


print(real_st)

path = [''] * len(real_st)

def abc(level):
    if level == len(real_st):
        return
    
    if ''.join(path) == target:
        print(path)
        
    for i in range(len(real_st)):
        path[level] = real_st[i]
        abc(level+1)

abc(0)