N = int(input())
book = [ input() for _ in range(N)]

ans = sorted(book, key=lambda x: (len(x),x))
for a in ans:
    print(a)