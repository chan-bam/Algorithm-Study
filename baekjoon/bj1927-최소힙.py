import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
hq = []

for _ in range(N):
    x = int(input())
    if x:
        heappush(hq, x)
    elif hq:
        print(heappop(hq))
    else:
        print(0)