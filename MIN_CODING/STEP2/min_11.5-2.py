
def Count():
    count = 0
    
    for lst in lsts:
        count += lst.count(num)
        
    return count

lsts = [
    [1,1,1],
    [1,2,1],
    [3,6,3]
]

num = int(input())

print( Count() )