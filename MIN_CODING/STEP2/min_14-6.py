vect = [3,5,1,1,2,3,2]

line = list(map(int,input().split()))

for i in range(len(line)):
    print(f'{line[i]}={vect.count(line[i])}개')
    