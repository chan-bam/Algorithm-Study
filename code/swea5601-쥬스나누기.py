import sys
sys.stdin = open("5601.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}', end=' ')
    for n in range(N):
        print(f'1/{N}', end=' ')
    print()