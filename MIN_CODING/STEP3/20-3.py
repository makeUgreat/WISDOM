arr = list(map(int,input().split()))

def recursion(index):
    
    if index == len(arr)-1:
        print(arr[index],end=' ')
        return
    
    print(arr[index],end=' ')
    
    recursion(index+1)
    print(arr[index],end=' ')


recursion(0)