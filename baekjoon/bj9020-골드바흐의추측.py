import sys
input = sys.stdin.readline

T = int(input().rstrip())

eratos = [1 for _ in range(10001)]
eratos[1] = 0

for i in range(2, 10001):
    for j in range(i * 2, 10001, i):
        eratos[j] = 0

for _ in range(T):
    n = int(input().rstrip())
    result = []
    minV = n
    if eratos[n // 2]:
        print(n // 2, n // 2)
    else:
        for i in range(2, n // 2):
            if eratos[i] and eratos[n - i]:
                if abs(n - i - i) < minV:
                    minV = abs(n - i - i)
                    result = [i, n - i]
        print(*result)


