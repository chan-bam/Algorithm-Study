import sys
input = sys.stdin.readline

N = int(input())
f = [0] * (N + 1)
f[1] = f[2] = 1
for i in range(3, N + 1):
    f[i] = f[i - 1] + f[i - 2]

print(f[N], N - 2)