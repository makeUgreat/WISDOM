arr = []
user_input = list(map(int,input().split()))

def input(user_input):
    for i in user_input:
        arr.append(i)
    return arr


def output(arr):
    for i in range( len(arr)-1, -1, -1 ):
        print(arr[i],end='')


def main():
    input(user_input)
    output(arr)

main()