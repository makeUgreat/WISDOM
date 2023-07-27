def find(ch):
    
    for i in range(len(lsts)):
        for j in range(len(lsts[i])):
            
            if lsts[i][j] == ch:
                return i,j
    
lsts = [
    ['A','D','F'],
    ['Q','W','E'],
    ['Z','X','C']
]

ch1 = input()
x,y = find(ch1)
print(f'{x},{y}')
