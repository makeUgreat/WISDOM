str_list = input().split()
index = 0
lsts = [[0]*3 for _ in range(2)]

for i in range(2):
    for j in range(3):
        lsts[i][j] = str_list[index]
        index += 1


def findUpper():
    upper_count = 0
    for lst in lsts:
        for k in lst:
            if k.isupper():
                upper_count += 1

    return upper_count 

def findLower():
    lower_count = 0
    for lst in lsts:
        for k in lst:
            if k.islower():
                lower_count += 1
    
    return lower_count

print(f'대문자{findUpper()}개')
print(f'소문자{findLower()}개')       