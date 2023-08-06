train = [3,7,6,4,2,9,1,7]
team = list(map(int,input().split()))

coverage = [] 
for t in team:
    coverage.append(train.index(t))
    
print(f'{min(coverage)}번~{max(coverage)}번 칸')