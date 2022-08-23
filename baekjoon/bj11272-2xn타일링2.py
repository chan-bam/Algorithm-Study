import sys
input = sys.stdin.readline

n = int(input())

D = [0, 1, 3]

if n >= len(D):
    for i in range(len(D), n + 1):
        D.append(D[i - 2] * 2 + D[i - 1])

print(D[n] % 10007)