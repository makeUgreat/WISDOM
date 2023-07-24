arr = [[3,4,1], [2,1,4], [3,3,0]]
odd_count = 0
even_count = 0

for i in arr:
    for j in i:
        if j % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print(f'짝수 : {even_count}')
print(f'홀수 : {odd_count}')
