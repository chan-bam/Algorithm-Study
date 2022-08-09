import sys
sys.stdin = open("11197in.txt")

T = int(input())

for tc in range(1, T+1):
    # 크기 N, 종류 M
    N, M = map(int, input().split())
    print(f'#{tc}')
    if M == 1:
        for i in range(1, N+1):
            print('*' * i)

    if M == 2:
        for i in range(N, 0, -1):
            print('*' * i)

    if M == 3:
        for i in range(N):
            for j in range(N*2):
                if N - i - 1 <= j <= N + i - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()

