import sys
sys.stdin = open("5431in.txt")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    submit_std = list(map(int, input().split()))
    std_num = list(range(1, N+1))

    for s in submit_std:
        std_num.remove(s)

    res = ' '.join(list(map(str, std_num)))

    print(f'#{tc} {res}')
