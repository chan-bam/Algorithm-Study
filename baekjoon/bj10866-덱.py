from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

deq = deque()

def solve(command):
    if command == 'pop_front':
        if deq:
            return deq.popleft()
        else:
            return -1
    elif command == 'pop_back':
        if deq:
            return deq.pop()
        else:
            return -1
    elif command == 'size':
        return len(deq)
    elif command == 'empty':
        if deq:
            return 0
        else:
            return 1
    elif command == 'front':
        if deq:
            return deq[0]
        else:
            return -1
    elif command == 'back':
        if deq:
            return deq[-1]
        else:
            return -1
    elif command.split()[0] == 'push_front':
        deq.appendleft(command.split()[1])
        return
    elif command.split()[0] == 'push_back':
        deq.append(command.split()[1])
        return

for _ in range(N):
    result = solve(input().rstrip())
    if result != None:
        print(result)