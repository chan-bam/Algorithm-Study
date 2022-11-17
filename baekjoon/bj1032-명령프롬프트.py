import sys
input = sys.stdin.readline
N = int(input())
files = [input() for _ in range(N)]
result = list(files[0])
L = len(result)

for i in range(1, N):
    for j in range(L):
        if result[j] != files[i][j]:
            result[j] = '?'
print(*result, sep='')