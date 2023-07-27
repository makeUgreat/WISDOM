lsts = [
    ['A','B','C','D','E','F','G'],
    [4,2,5,1,6,7,3]
]

start_index = 0
destination_index = 0
distance = 0

ch1, ch2 = input().split()
for i in range(len(lsts[0])):
    if lsts[0][i] == ch1:
        start_index = i
    
    if lsts[0][i] == ch2:
        destination_index = i

if start_index < destination_index:
    for j in range(start_index+1,destination_index):
        distance += lsts[1][j]  
elif start_index > destination_index:
    for j in range(destination_index+1,start_index):
        distance += lsts[1][j]  

print(distance)
    

