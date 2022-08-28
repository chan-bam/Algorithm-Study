import sys
input = sys.stdin.readline
from heapq import heappush, heappop

T = int(input())
for _ in range(T):
    N = int(input())
    min_hq, max_hq = [], []
    visited = [-1] * 1_000_001
    for i in range(N):
        c, n = input().split()
        visited[i] = 0
        if c == 'I':
            heappush(min_hq, (int(n), i))
            heappush(max_hq, (-int(n), i))
        else:
            if n == '-1' and min_hq: # c == 'D' and n == '-1'
                visited[min_hq[0][1]] = 1
                heappop(min_hq)
            elif max_hq: # c == 'D' and n == '1'
                visited[max_hq[0][1]] = 1
                heappop(max_hq)
            while max_hq and visited[max_hq[0][1]]:
                heappop(max_hq)
            while min_hq and visited[min_hq[0][1]]:
                heappop(min_hq)

    if min_hq and max_hq:
        print(-max_hq[0][0], min_hq[0][0])
    else:
        print('EMPTY')
'''
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

T = int(input())
for _ in range(T):
    N = int(input())
    min_hq, max_hq = [], []
    visited = [-1] * 1_000_001
    for i in range(N):
        c, n = input().split()
        visited[i] = 0
        if c == 'I':
            heappush(min_hq, (int(n), i))
            heappush(max_hq, (-int(n), i))
        elif n == '-1': # c == 'D' and n == '-1'
            while min_hq and visited[min_hq[0][1]]:
                heappop(min_hq)
            if min_hq: 
                visited[min_hq[0][1]] = 1
                heappop(min_hq)
        else: # c == 'D' and n == '1'
            while max_hq and visited[max_hq[0][1]]:
                heappop(max_hq)
            if max_hq:
                visited[max_hq[0][1]] = 1
                heappop(max_hq)
    while max_hq and visited[max_hq[0][1]]:
        heappop(max_hq)
    while min_hq and visited[min_hq[0][1]]:
        heappop(min_hq)

    if min_hq and max_hq:
        print(-max_hq[0][0], min_hq[0][0])
    else:
        print('EMPTY')
'''