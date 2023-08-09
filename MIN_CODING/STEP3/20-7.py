index = int(input())
arr = [3,7,4,1,9,4,6,2]

def abc(index):

    if index == 0:
        print(arr[index],end=' ')
        return
    
    print(arr[index],end=' ')
    abc(index-1)
    print(arr[index],end=' ')

abc(index)