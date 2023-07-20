user_input = int(input())
list = []

def main(user_input):
    for i in range(user_input, user_input + 6):
        list.append(i)
    PrintAll()


def PrintAll():
    print(*list,sep='\n')


main(user_input)