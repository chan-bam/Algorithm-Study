N, K = map(int, input().split())

coin = [int(input()) for _ in range(N)]
cnt = 0

for i in range(N - 1, -1, -1):
    if K // coin[i] > 0:
        cnt += K // coin[i]
        K = K % coin[i]

print(cnt)