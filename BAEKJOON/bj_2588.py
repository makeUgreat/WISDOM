a1,b1,c1 = map(int, input())
a2,b2,c2 = map(int, input())

line1 = int( (a1*100) + (b1*10) + c1 )
line2 = int( (a2*100) + (b2*10) + c2 )
  
print( line1 * c2 )
print( line1 * b2 )
print( line1 * a2 )

total_sum = (line1 * c2) + ((line1 * b2)*10) + ((line1 * a2) * 100);
print(total_sum)