lsts = [
    ['A','B','C'],
    ['A','G','H'],
    ['H','I','J'],
    ['K','A','B'],
    ['A','B','C']
]

tmp = []
for row in lsts:
    tmp.extend(map(ord,(row)))

bucket = [0] * (max(tmp) + 1)
for t in range(len(tmp)):
    bucket[tmp[t]] += 1

# DAT(bucket)을 바탕으로 누적합해서 정렬하기 

for i in range(1, len(bucket)):
    bucket[i] += bucket[i-1]
    
    
sorted_list = [0] * len(tmp)


for element in tmp:
    bucket[element] -= 1
    sorted_list[ bucket[element] ] = chr(element)
    

print(*sorted_list,sep='') 
