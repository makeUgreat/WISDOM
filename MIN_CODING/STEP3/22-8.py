arr = [
    [
    [2,4],
    [1,5]
    ],

    [
    [2,3],
    [3,6]
    ],

    [
    [7,3],
    [1,5]
    ]
]

num = int(input())
max_v = -21e8
min_v = 21e8


for i in range(2):
    for k in range(2):
        current_num = arr[num][i][k]
        if current_num > max_v:
            max_v = current_num
        if current_num < min_v:
            min_v = current_num

print(f'MAX={max_v}')
print(f'MIN={min_v}')
        
        
