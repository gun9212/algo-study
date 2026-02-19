import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
C = list(map(int, input().split()))

best = 0
for j in combinations(C, 3):
    s = sum(j)
    if best < s <= M:
        best = s

print(best)