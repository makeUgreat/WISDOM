
def INPUT(a, b):
    OUTPUT(a, b)

def OUTPUT(a,b):
    print(f'{a} {b}')
    

user_input = input().split()
INPUT(*user_input)