import sys
sys.stdin = open('MIN_CODING/for_min_input.txt','r')

lsts = [] 
for i in range(5):
    line = list(map(int,input().split()))
    lsts.append(line)


for lst in lsts:
    print(sum(lst),end=' ')