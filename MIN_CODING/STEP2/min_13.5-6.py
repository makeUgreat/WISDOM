def FindABC(ch1,ch2):
    count_A = 0
    count_B = 0
    count_C = 0

    count_A += ch1.count('A')
    count_A += ch2.count('A')
    count_B += ch1.count('B')
    count_B += ch2.count('B')
    count_C += ch1.count('C')
    count_C += ch2.count('C')


    print(f'A:{count_A}')
    print(f'B:{count_B}')
    print(f'C:{count_C}')

ch1 = input()
ch2 = input()

FindABC(ch1,ch2)