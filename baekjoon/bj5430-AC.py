import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    func = input().rstrip()
    n = int(input())
    if n:
        arr = input()[1:-2].rstrip().split(',') # 문자열로 받아도 됨
    else:
        arr = input()
        arr = []

    result = ''
    status = 1 # 순방향

    queue = deque(arr)

    for f in func:
        if f == 'R':
            status ^= 1
        else: # 'D'
            if queue and status:
                queue.popleft()
            elif queue and not status:
                queue.pop()
            else:
                result = 'error'
                break

    if result:
        print(result)
    else:
        if not status:
            queue.reverse()
        print('[' + ','.join(queue) + ']')

'''
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    func = input().rstrip()
    n = int(input())

    result = ''
    status = 1 # 순방향

    if n:
        arr = input()[1:-2].rstrip().split(',')
    else:
        arr = input()
        arr = []

    for f in func:
        if f == 'R':
            status ^= 1
        else: # 'D'
            if arr and status:
                arr.pop(0)
            elif arr and not status:
                arr.pop(-1)
            else:
                result = 'error'

    if result:
        print(result)
    else:
        print('[', end='')
        if not status:
            arr.reverse()
        print(*arr, sep=',', end='')
        print(']')
'''