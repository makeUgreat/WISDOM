# def getSum(startIndex,lst):
#     sum_ = 0
#     for i in range(5):
#         sum_ += lst[startIndex + i]

#     return sum_


# lst =[3,4,1,1,2,6,8,7,8,9,10]
# startIndex = int(input())

# print(getSum(startIndex,lst))


def getSum(startIndex,lst):
    sum_ = sum(lst[startIndex:startIndex + 5])

    return print(sum_)

lst = [3,4,1,1,2,6,8,7,8,9,10]
startIndex = int(input())

getSum(startIndex,lst)