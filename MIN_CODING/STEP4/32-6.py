from collections import Counter
N, M = map(int,input().split())
vote = [list(input().split()) for _ in range(M)]
vote_counts = Counter(candidate for candidate, _ in vote)
ans = sorted(vote_counts.items(), key=lambda x: -x[1])

most = ans[0][0]


push = []
for vo in vote:
    if vo[0] == most:
        push.append(vo[1])

print(*push)
