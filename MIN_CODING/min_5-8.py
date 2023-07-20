global_variable = 0

def KFC(number):
    global global_variable
    global_variable = number
    return global_variable
    

def BBQ(number):
    if global_variable > 5:
        print("만세")
    else:
        print("다시")


def main():
    num = int(input())
    result = KFC(num)
    BBQ(result)

if __name__ == "__main__":
    main()