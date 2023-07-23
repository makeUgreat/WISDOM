arr = ['A', 'B', 'C']

def KFC(num):
    for i in range(num):
        print(*arr,sep='')

def main():
    num = int(input())
    KFC(num)


main()