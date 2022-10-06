import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque([])

for _ in range(N):
    operation = input().rstrip()
    if operation.split()[0] == 'push':
        queue.append(int(operation.split()[1]))
    elif operation == 'size':
        print(len(queue))
    elif operation == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif operation == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif operation == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif operation == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)