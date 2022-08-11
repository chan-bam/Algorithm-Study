import sys
input = sys.stdin.readline

N = int(input())

Q = []

for _ in range(N):
    command = input().rstrip()
    if command == 'pop': # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(Q):
            print(Q.pop(0))
        else:
            print(-1)
    elif command == 'size': # 큐에 들어있는 정수의 개수를 출력한다.
        print(len(Q))
    elif command == 'empty': # 큐가 비어있으면 1, 아니면 0을 출력한다.
        if len(Q):
            print(0)
        else:
            print(1)
    elif command == 'front': # 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(Q):
            print(Q[0])
        else:
            print(-1)
    elif command == 'back': # 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(Q):
            print(Q[-1])
        else:
            print(-1)
    else: # push X # 정수 X를 큐에 넣는 연산
        Q.append(command.split()[-1])

