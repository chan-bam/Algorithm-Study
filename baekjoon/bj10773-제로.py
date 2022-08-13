import sys
input = sys.stdin.readline

K = int(input())
result = []

for _ in range(K):
    N = int(input())
    if N == 0:
        result.pop()
    else:
        result.append(N)

print(sum(result))
