# 앞에서부터 짜기
# 시간초과

import sys
sys.stdin = open("1859.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))
    benefit = 0

    for i in range(N-1):
        maxV = cost[i+1] # 판매가 가능한 첫번째날로 초기화
        for j in range(i+1, N):
            if cost[j] > maxV:
                maxV = cost[j]
        if cost[i] < maxV:
            benefit += (maxV - cost[i])
    print(f'#{tc} {benefit}')