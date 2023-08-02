def isExist(get_chr,get_lst):
    return get_chr in get_lst


lst = ['M','T','K','C']
ch1 = input()

if isExist(ch1,lst):
    print('발견')
else:
    print('미발견')
