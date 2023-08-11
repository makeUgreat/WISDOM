nums = map(int,input().split())

triple = []

for i in range(3):
    line = [ [t]*3 for t in nums ]
    triple.append(line)




for sec in triple:
    for one in sec:
        print(*one)
    print()