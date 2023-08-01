import sys
sys.stdin = open('input.txt','r')

lsts = []
for _ in range(3):
    line = input()
    lsts.append(line[-1])


print(*lsts,sep='')

