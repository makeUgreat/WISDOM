x = int(input())
arr = []

i = x
count = 0
while count <= 5:
    arr.append(i)
    i += x
    count += 1


print(*arr,sep=' ')


# for 사용
'''
x = int(input())
arr = []

for count in range(6):
    arr.append(x * (count + 1))

print(*arr, sep=' ')
'''