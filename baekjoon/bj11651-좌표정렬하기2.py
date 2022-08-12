import sys
input = sys.stdin.readline

N = int(input())

result = []
for _ in range(N):
    x, y = map(int, input().split())
    result.append([y, x])

result.sort()

for res in result:
    print(res[1], res[0])