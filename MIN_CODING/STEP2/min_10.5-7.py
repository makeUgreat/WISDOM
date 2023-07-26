def aToZ():
    ch1 = ord(input())
    gap_toA = abs(ch1-ord('A'))
    gap_toZ = abs(ch1-ord('Z'))

    if gap_toA < gap_toZ:
        print('A')
    elif gap_toA > gap_toZ:
        print('Z')



aToZ()