arr1 = ['B', 'D', 5, 'Q', 'A']
arr2 = ['Q', 'E', 'R', 'E', 'F']

def input_func():
    char1 = input()

    return char1

def output_func(x):
    if x.islower():
        print(*arr1,sep='',end='')
    elif x.isupper():
        print(*arr2,sep='',end='')
    elif x.isnumeric():
        print("HGFEDCBA")


output_func(input_func())