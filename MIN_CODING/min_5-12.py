def QTR():
    print("QTR100%")


def BBQ():
    print("BBQ100%")

list_sum = sum(list(map(int,input().split())))

if list_sum >= 10:
    QTR()
else:
    BBQ()
