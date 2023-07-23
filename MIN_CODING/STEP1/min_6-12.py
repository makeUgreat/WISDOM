def process(a, b, c):
    if a == 'A' and b == 'B' and c == 'C':
        global flag
        flag += 1
    output()
        
        
def output():
    if flag == 1:
        print("ABC를찾았다")
    else:
        print("못찾았다")
        
        
a, b, c = input().split()
flag = 0

process(a, b, c)