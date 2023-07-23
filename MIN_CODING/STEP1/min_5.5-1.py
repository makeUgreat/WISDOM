def KFC():
    print("KFC")


def BBQ():
    print("BBQ")

x = input()

if x == 'B':
    KFC()
    BBQ()
elif x == 'b':
    BBQ()
elif x == '7':
    KFC()