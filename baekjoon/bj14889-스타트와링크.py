import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = sys.maxsize

for pick in combinations(range(N), N // 2):
    temp1, temp2 = 0, 0
    for i, j in combinations(pick, 2):
        temp1 += (arr[i][j] + arr[j][i])
    none_pick = set(range(N)) - set(pick)
    for i, j in combinations(none_pick, 2):
        temp2 += (arr[i][j] + arr[j][i])
    result = min(result, abs(temp1 - temp2))
print(result)