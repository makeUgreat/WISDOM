lsts = [
    ['P','O','T','I','O'],
    ['A','B','C','D','E'],
    ['Y','O','U','R','E']
]

a,b = map(int,input().split())

for i in range(0,b+1):
    for j in range(a,b+1):
            try:
                print(lsts[i][j],end='')
            except IndexError:
                pass
            

        