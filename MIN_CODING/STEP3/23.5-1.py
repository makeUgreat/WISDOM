def abc(level):
    
    print(arr[level],end=' ')
    
    if level == 4:
        return
    
    abc(level+1)
    
arr = [3,5,1,9,7]

for _ in range(4):
    st = input()

    if st == 'R':
        tmp = arr.pop()
        arr.insert(0,tmp)

    if st == 'L':
        tmp = arr.pop(0)
        arr.append(tmp)

abc(0)

