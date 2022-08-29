import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

res = 0
while N > 0:
    N -= 1
    acc = (2 ** N) ** 2
    if r < 2 ** N and c < 2 ** N:
        res += acc * 0
    elif r < 2 ** N and 2 ** N <= c:
        res += acc * 1
        c -= 2 ** N
    elif 2 ** N <= r and c < 2 ** N:
        res += acc * 2
        r -= 2 ** N
    elif 2 ** N <= r and 2 ** N <= c:
        res += acc * 3
        r -= 2 ** N
        c -= 2 ** N

print(res)