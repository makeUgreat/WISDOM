def calculator():
    score = int(input())

    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    else:
        return 'D'
    

print(calculator())