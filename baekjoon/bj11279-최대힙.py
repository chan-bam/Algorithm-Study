import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
hq = []

for _ in range(N):
    x = int(input())
    if not x and hq:
        print(heappop(hq)[1])
    elif not x:
        print(0)
    else:
        heappush(hq, (-x, x))
