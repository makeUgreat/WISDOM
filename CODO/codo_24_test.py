import sys
sys.stdin = open("input.txt","r")


text = input().split()
count = 0

for i in range(len(text)):
    text[i] = text[i].strip(",")
    text[i] = text[i].strip("-")
    text[i] = text[i].strip(".")
    text[i] = text[i].strip("'")
    if text[i] == 'the':
        count += 1

print(count)


# print( text.count('the') )