arr =[0,1]

def fib(n):
    
    for i in range(n-1):
        arr.append(arr[i] + arr[i+1])
        
    
    return(max(arr))


n = int(input())
print(fib(n))

'''
재귀함수로 피보나치 수열

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
'''