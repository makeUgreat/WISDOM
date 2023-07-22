def solve(a):
    
    return sum(a)

a = []
for i in range( int(input())+1 ) :
    if 1 <= i <= 3000000:
        a.append(i)

print(solve(a))  
    