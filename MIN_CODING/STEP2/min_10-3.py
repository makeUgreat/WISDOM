def KFC():
    result_chicken = chicken()
    result_coke = coke()
    
    print(f'{result_chicken}{result_coke}')
    
def chicken():
    num = int(input())
    
    return (num + 10)
    
def coke():
    ch1 = input()
    return ch1

KFC()