lst = ['A','T','K','P','T','C','A','B','C']

word = input().split()
front_index = 0
rear_index = 0

for i in range(len(lst)):
    if lst[i] == word[0]:
        front_index = i
        break
for j in range(len(lst)-1,-1,-1):
    if lst[j] == word[-1]:
        rear_index = j
        break

print( abs(front_index-rear_index) )
