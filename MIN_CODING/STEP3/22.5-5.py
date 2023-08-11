def findMAP(get_y,get_x):
    
    y = dict.get(get_y,-1)
    x = int(get_x)-1

    return MAP[y][x]

    


MAP = [
    [3,5,4,2,2,3],
    [1,3,3,3,4,2],
    [5,4,4,2,3,5]
]
price = ['T','P','G','K','C']

dict ={
    'A': 0,
    'B': 1,
    'C': 2
}


get_y,get_x = input().split()
coordinate = findMAP(get_y,get_x)

print(price[coordinate-1])
