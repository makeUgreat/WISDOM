h,m = map(int, input().split())


M_transFromH = h * 60 

if h == 0:
  M_transFromH = 24 * 60

if 0 <= h <= 23:
  if 0 <= m <= 59:
    M_transFromH += m - 45
  

    if int(M_transFromH // 60) == 24:
      print( 0 , int(M_transFromH % 60) )
    else:
      print( int(M_transFromH // 60) , int(M_transFromH % 60) )
      
  else:
    pass
else:
  pass