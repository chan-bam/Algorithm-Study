import sys
input = sys.stdin.readline
from heapq import heappush, heappop

T = int(input())

for _ in range(T):
    N = int(input())
    min_hq, max_hq = [], []
    visited = [0] * 1_000_001
    for i in range(N):
        c, n = input().split()
        if c == 'I':
            heappush(min_hq, (int(n), i))
            heappush(max_hq, (-int(n), i))
            visited[i] = 1
        elif c == 'D' and n == '-1': # elif n == '-1':
            while min_hq and not visited[min_hq[0][1]]:
                heappop(min_hq)
            if min_hq:
                visited[min_hq[0][1]] = 0
                heappop(min_hq)
        elif c == 'D' and n == '1': # else:
            while max_hq and not visited[max_hq[0][1]]:
                heappop(max_hq)
            if max_hq:
                visited[max_hq[0][1]] = 0
                heappop(max_hq)
    while min_hq and not visited[min_hq[0][1]]:
        heappop(min_hq)
    while max_hq and not visited[max_hq[0][1]]:
        heappop(max_hq)
    if min_hq and max_hq:
        print(-max_hq[0][0], min_hq[0][0])
    else:
        print('EMPTY')