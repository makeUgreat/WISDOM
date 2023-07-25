def BBQ(num2):
    for i in range(1,num2+1):
        print(i,end='')
        
def KFC(ch1):
    for i in range(7):
        print(ch1,end='')
    

num = int(input())

if num % 2 == 1:
    num2 = int(input())
    BBQ(num2)
elif num % 2 == 0:
    ch1 = input()
    KFC(ch1)
    
    