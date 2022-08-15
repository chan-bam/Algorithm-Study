import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen_and_see = {}

for _ in range(N):
    listen = input().rstrip()
    listen_and_see[listen] = 0

for _ in range(M):
    see = input().rstrip()
    if see in listen_and_see:
        listen_and_see[see] += 1

result = []

for key, value in listen_and_see.items():
    if value:
        result.append(key)

result.sort()
print(len(result))
for r in result:
    print(r)