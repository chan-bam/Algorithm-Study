import sys
sys.stdin = open("1859in.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cost = list(map(int, input().split()))
    benefit = 0
    # 뒤에서부터 비교해서 짜는 방식
    maxV = cost[N-1]
    for i in range(N-1, -1, -1):
        if maxV < cost[i]:
            maxV = cost[i]
        else:
            benefit += maxV - cost[i]
    print(f'#{tc} {benefit}')