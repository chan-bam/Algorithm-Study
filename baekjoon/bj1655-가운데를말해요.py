import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
leftheap, rightheap = [], []
# leftheap : 최대힙, 중간보다 같거나 작은 값 # leftheap의 루트가 중간값
# rightheap : 최소힙, 중간보다 큰 값

for i in range(N):
    num = int(input())
    if i % 2:
        heappush(rightheap, num)
    else:
        heappush(leftheap, -num)
    if i and -leftheap[0] > rightheap[0]: # 교환
        heappush(rightheap, -heappop(leftheap))
        heappush(leftheap, -heappop(rightheap))
    print(-leftheap[0])