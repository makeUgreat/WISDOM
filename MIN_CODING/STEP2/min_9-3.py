lsts = ['A', 'F', 'G', 'A', 'B', 'C']

ch1, ch2 = input().split()

if ch1 in lsts and ch2 in lsts:
    print("와2개")
elif ch1 in lsts or ch2 in lsts:
    print("오1개")
else:
    print("우0개")