import sys
input = sys.stdin.readline

M = int(input().rstrip())

S = []
allS = [str(i) for i in range(1, 21)]

for _ in range(M):
    command = input().rstrip()
    if command == 'all':
        S = allS[:]
    elif command == 'empty':
        S = []
    else:
        command, X = command.split()
        if command == 'add':
            if X not in S:
                S.append(X)
        elif command == 'remove':
            if X in S:
                S.remove(X)
        elif command == 'check':
            if X in S:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if X in S:
                S.remove(X)
            else:
                S.append(X)
