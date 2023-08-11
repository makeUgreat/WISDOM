bucket = [0] * 11
for i in range(4):
    st = input()

    bucket[len(st)] = st


for i in bucket:

    if i != 0:
        print(i)