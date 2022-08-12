import sys
input = sys.stdin.readline

N = int(input())

result = [0 for _ in range(10001)]
for _ in range(N):
    result[int(input().rstrip())] += 1 # counting

for idx in range(len(result)):
    if result[idx]:
        for _ in range(result[idx]):
            print(idx)

