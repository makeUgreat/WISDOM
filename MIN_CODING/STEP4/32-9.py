from collections import Counter

cards = list(input())
N = int(input())

cards.sort()
cards2 = cards[-6:]

nums = Counter(cards2)
ans = sorted(nums.items(), key=lambda x: (-x[1],x[0]))
print(ans[0][0])