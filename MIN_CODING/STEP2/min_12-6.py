def Length():
    ch1 = input()
    ch2 = input()
    ch3 = input()

    for i in range(len(lsts)):
        if lsts[i] == ch1:
            print(f'{ch1}={i}')
        if lsts[i] == ch2:
            print(f'{ch2}={i}')
        if lsts[i] == ch3:
            print(f'{ch3}={i}')
 

lsts = ['M','I','N','Q','U','E','S','T']


Length()