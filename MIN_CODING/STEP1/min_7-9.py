lst = map(int,input().split())

for j in range(1,6): 
    for i in lst:
        if i >= 70:
            print(f"{j}번사람은{i}점PASS")
            break
        elif i >= 50:
            print(f"{j}번사람은{i}점RETEST")
            break
        else:
            print(f"{j}번사람은{i}점FAIL")
            break
        