table = [
    ['Jason'],
    ['Dr.tom'],
    ['EXEXI'],
    ['GK12P'],
    ['POW']
]

password = input()
exist = 0
for element in table:
    if ''.join(element) == password:
        exist = 1


if exist: print('암호해제')
else: print('암호틀림')