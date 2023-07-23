char = input() # A: 65
gap_int = ord(char) - 65


for i in range(gap_int+1):
    print( chr(65 + i),end='') 