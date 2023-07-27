def moom():
    age = int(input())
    res_1 = age-4
    res_2 = age+3
    res_3 = age*2
    
    return res_1, res_2 ,res_3


result = moom()
print(*result)
