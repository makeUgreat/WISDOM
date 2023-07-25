lst = list(map(int,input().split()))

for index, score in enumerate(lst):
    if score < 5:
        print(f"{index}번은 {score}점 불합격")
    elif score >= 5:
        print(f"{index}번은 {score}점 합격")

