import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    D = [0, 1, 1, 1, 2, 2]
    N = int(input().rstrip())
    if N >= len(D):
        for i in range(len(D), N + 1):
            D.append(D[i - 1] + D[i - 5])
    print(D[N])