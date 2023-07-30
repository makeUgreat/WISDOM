lsts = ['A','B','C','Z','E','T','Q']

members = list(input())

for member in members:
    if member in lsts:
        print(f'{member}=마을사람')
    if member not in lsts:
        print(f'{member}=외부사람')
        