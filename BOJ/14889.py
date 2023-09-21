import sys
sys.stdin = open('input.txt','r')

from itertools import combinations

n = int(input())
s = [[0]*(n+1)] + [ [0] + list(map(int,input().split())) for _ in range(n) ]

member = [i for i in range(1,n+1)]

teamA = []
teamB = []
min_v = 21e8
for teamA in combinations(member,n//2):
    teamB = list(set(member) - set(teamA))

    powerA = 0
    powerB = 0
    for team in combinations(teamA,2):
        powerA += (s[team[0]][team[1]] + s[team[1]][team[0]])
    for team in combinations(teamB,2):
        powerB += (s[team[0]][team[1]] + s[team[1]][team[0]])

    gap = powerA-powerB
    min_v = min(min_v,abs(gap))

print(min_v)
