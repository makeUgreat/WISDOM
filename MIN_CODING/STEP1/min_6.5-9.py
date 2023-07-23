lst = [5,4,1,2,7,8]
rev_lst = []
n = int(input())

for i in range(n):
    rev_lst.clear()
    for j in range( len(lst)-1 , -1, -1):
        rev_lst.append(lst[j])
        
    print(*rev_lst,end='')
    print()