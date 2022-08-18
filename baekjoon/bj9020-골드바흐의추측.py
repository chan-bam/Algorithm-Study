import sys
input = sys.stdin.readline

T = int(input().rstrip())

eratos = [1 for _ in range(10001)]

for i in range(2, 10001):
    for j in range(i * 2, 10001, i):
        eratos[j] = 0

for _ in range(T):
    n = int(input().rstrip())
    if eratos[n // 2]:
        print(n // 2, n // 2)
    else:
        for i in range(n // 2 + 1, n - 1):
            if eratos[i] and eratos[n - i]:
                print(n - i, i)
                break
        # for i in range(n // 2 - 1, 2, -1):
        #     if eratos[i] and eratos[n - i]:
        #         print(i, n - i)
        #         break
