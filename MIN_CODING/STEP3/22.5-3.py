ch = ord(input())

triple = []

for i in range(3):
    lsts = [ [chr(ch+i)] *3 for _ in range(3)]
    triple.append(lsts)



for sec in triple:
    for one in sec:
        print(*one,sep='')
    print()