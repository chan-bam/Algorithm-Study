import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())

hq = []
for _ in range(N):
    x = int(input())
    if x:
        heappush(hq, (abs(x), x))
    elif hq:
        print(heappop(hq)[1])
    else:
        print(0)