lsts = ['A', '1', '1', '1', '5', 'A', 'w', 'z']

ch1 = input()

if lsts.count(ch1) >= 3:
    print('THREE')
elif lsts.count(ch1) >= 2:
    print('TWO')
elif lsts.count(ch1) >= 1:
    print('ONE')
elif lsts.count(ch1) == 0:
    print('NOTHING')