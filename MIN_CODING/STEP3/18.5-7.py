vect = 'MINCODING'
n = int(input())
chars = input().split()

vect = set(vect)

cnt = {}
for chr in vect:
    cnt[chr] = cnt.get(chr,0) + 1

for chr in chars:
    if cnt.get(chr,0):
        print('O',end='')
    else:
        print('X',end='')